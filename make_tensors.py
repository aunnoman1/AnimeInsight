
import pyodbc
import tensorflow as tf
from joblib import load
import pandas as pd
import numpy as np
import urllib
import sqlalchemy


# Connect to MSSQL database

driver= '{ODBC Driver 17 for SQL Server}'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AnimeInsight;UID=sa;PWD=12345678;Trusted_Connection=yes')

cursor = connection.cursor()



df = pd.read_sql('SELECT * FROM anime_metadata', connection)



connection.close()






# Load your TensorFlow model
model = tf.keras.models.load_model('models/anime_model.keras')



mean_score_scaler=load('preprocessing/mean_score_scaler.pkl')

rating_scaler=load('preprocessing/rating_scaler.pkl')

score_scaler=load('preprocessing/score_scaler.pkl')

type_encoder=load('preprocessing/Type_encoder.pkl')


gender_encoder=load('preprocessing/gender_encoder.pkl')

user_input_shape=6

anime_input_shape=8

studio_max_length = 10

genre_max_length=9

source_max_length=1


@tf.keras.utils.register_keras_serializable()
def split_func(input_str):
  return tf.strings.split(input_str, sep=", ")


studio_vectorize_layer_model=tf.keras.models.load_model('preprocessing/studio_vectorize_layer_model')
studio_vectorize_layer = studio_vectorize_layer_model.layers[0]

num_studios=len(studio_vectorize_layer.get_vocabulary())



genre_vectorize_layer_model=tf.keras.models.load_model('preprocessing/genre_vectorize_layer_model')
genre_vectorize_layer = genre_vectorize_layer_model.layers[0]

num_genres=len(genre_vectorize_layer.get_vocabulary())



source_vectorize_layer_model=tf.keras.models.load_model('preprocessing/source_vectorize_layer_model')
source_vectorize_layer = source_vectorize_layer_model.layers[0]


num_sources=len(source_vectorize_layer.get_vocabulary())



df.drop(['English_name',"Name",'Synopsis','Age_Rating','Rank','Scored_By','Status','Premiered','Episodes','Duration','Licensors','Producers' , 'Aired','Image_URL'],axis=1,inplace=True)


df.fillna({'Score':df['Score'].mean()},inplace=True)


df.loc[:,'Score']=score_scaler.transform(df[['Score']]).astype(np.float32)


encoded_Types = type_encoder.transform(df[['Type']])  # Fit and transform the column
encoded_df = pd.DataFrame(encoded_Types.toarray(), columns=type_encoder.categories_[0],index=df.index)  # Create a DataFrame from the encoded columns

df=pd.concat([df, encoded_df], axis=1)  # Concatenate the original DataFrame with the encoded DataFrame
df.drop(['Type'],axis=1,inplace=True)


df.fillna({'Studios':'','Genres':'','Source':''},inplace=True)




sequences=studio_vectorize_layer(df.loc[:,'Studios'])
padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=studio_max_length, padding='post')

# Create separate columns for each index in the sequence
for i in range(studio_max_length):
    df[f'Studio_Index_{i+1}'] = padded_sequences[:, i]

df.drop('Studios', axis=1, inplace=True)


sequences=genre_vectorize_layer(df.loc[:,'Genres'])

padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=genre_max_length, padding='post')

# Create separate columns for each index in the sequence
for i in range(genre_max_length):
    df[f'Genre_Index_{i+1}'] = padded_sequences[:, i]

df.drop('Genres', axis=1, inplace=True)


sequences=source_vectorize_layer(df.loc[:,'Source'])

padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=source_max_length, padding='post')

# Create separate columns for each index in the sequence
for i in range(source_max_length):
    df[f'Source_Index_{i+1}'] = padded_sequences[:, i]

df.drop('Source', axis=1, inplace=True)


anime_columns=df.iloc[:,1:1+anime_input_shape].to_numpy(dtype='float32')
anime_studio_embedding_columns = df.iloc[:,1+anime_input_shape:1+anime_input_shape+studio_max_length].to_numpy()
anime_genre_embedding_columns= df.iloc[:,1+anime_input_shape+studio_max_length:1+anime_input_shape+studio_max_length+genre_max_length].to_numpy()
anime_source_embedding_columns = df.iloc[:,-1:].to_numpy()


input={'anime_inputs':anime_columns,'anime_genre_embeddings_inputs':anime_genre_embedding_columns,'anime_studio_embeddings_inputs':anime_studio_embedding_columns,'anime_source_embeddings_inputs':anime_source_embedding_columns}


output=model(input)


output_df = pd.DataFrame(output,columns=['tensor_1', 'tensor_2', 'tensor_3', 'tensor_4', 'tensor_5', 'tensor_6', 'tensor_7', 'tensor_8', 'tensor_9', 'tensor_10', 'tensor_11', 'tensor_12', 'tensor_13', 'tensor_14', 'tensor_15', 'tensor_16'])


final_df =pd.concat([df['anime_id'], output_df], axis=1)


final_df.rename(columns={'anime_id':'AnimeID'},inplace=True)





'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AnimeInsight;UID=sa;PWD=12345678;Trusted_Connection=yes'
connect_string = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};Server=localhost;Database=AnimeInsight;UID=sa;PWD=12345678;Trusted_Connection=yes')
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={connect_string}', fast_executemany=True)

with engine.connect() as connection:
  final_df.to_sql('anime_tensors', connection, index=False, if_exists='append')





