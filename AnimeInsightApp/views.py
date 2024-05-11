from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.db import connection
from django.conf import settings
from .models import User,FavGenres,Profile
import logging
import os

import numpy as np
import pandas as pd
import tensorflow as tf
from joblib import load
import threading

logger = logging.getLogger(__name__)

# Create your views here.

@login_required
def home(request):
    context={}
    if request.method=='GET':
        return render(request, 'AnimeInsightApp/Home.html')
    
def login_request(request):
    context={}
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            profile=Profile.objects.get(userid=user)
            if(profile.registered):
                return redirect("AnimeInsightApp:home")
            else:
                return redirect('AnimeInsightApp:complete_profile')
        else:
            context['message']="Invalid username or password."
            return render(request, 'AnimeInsightApp/login.html', context)
    else:
        return render(request,'AnimeInsightApp/login.html',context)


def register(request):
    context={}
    if request.method=="POST":
        username = request.POST['username']
        password= request.POST['password1']
        password2=request.POST['password2']
        email = request.POST['email']
        user_exists=False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
            context['message']="user already exists"
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        if( password !=password2):
            context['message']="password does not match"
            return render(request,"AnimeInsightApp/registration.html",context)

        # If it is a new user
        if not user_exists:
            user = User.objects.create_user(username=username,password=password,email=email)
            profile =Profile(userid=user)
            profile.save()
            login(request,user)
            return redirect("AnimeInsightApp:complete_profile")
        else:
            return render(request,'AnimeInsightApp/registration.html',context)
    else:
        return render(request,'AnimeInsightApp/registration.html',context)

@login_required     
def complete_profile(request):
    context={}
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        selected_genres = request.POST.getlist('genres')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        for genre in selected_genres:
            FavGenres.objects.create(userid=user, genre=genre)

        profile = Profile.objects.get(userid=user)
        profile.dob=date_of_birth
        profile.registered=True
        profile.save()
        t= threading.Thread(target=recommend_anime,args=[request])
        return redirect('AnimeInsightApp:home')


    else:
        context['genres']=[g[0] for g in FavGenres.genre.field.choices]
        return render(request,'AnimeInsightApp/complete_profile.html',context)
    

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('AnimeInsightApp:login_request')

        
def recommend_anime(request):
    user_id=request.user.id
    user_mean_score= 8
    
    cursor = connection.cursor()
    # Step 1: Retrieve the user's favorite genres
    cursor.execute("SELECT genre FROM AnimeInsightApp_favgenres WHERE userid_id = %s", [user_id])
    fav_genres = cursor.fetchall()

    # Step 2: Get the top 50 anime for each genre from the animemetadata table
    anime_list = []
    for fav_genre in fav_genres:
        cursor.execute("""
            SELECT top 50 anime_id, Score,	Genres,	Type , Studios , Source
            FROM Anime_Metadata
            WHERE genre LIKE %s
            order by Score DESC
        """, ['%' + fav_genre[0] + '%'])
        anime_list.extend(cursor.fetchall())

    
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(anime_list, columns=columns)

    # Step 3: Use the TensorFlow model to predict ratings for each anime
    model_path=os.path.join(settings.MODELS,'merged_model.keras')
    model = tf.keras.models.load_model(model_path)
    preprocesing_path = settings.PREPROCESSING
    mean_score_scaler=load(preprocesing_path+'/mean_score_scaler.pkl')
    rating_scaler=load(preprocesing_path+'/rating_scaler.pkl')
    score_scaler=load(preprocesing_path+'/score_scaler.pkl')
    type_encoder=load(preprocesing_path+'/Type_encoder.pkl')
    gender_encoder=load(preprocesing_path+'/gender_encoder.pkl')
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

    
    df.fillna({'Score':df['Score'].mean()},inplace=True)

    df.loc[:,'Score']=score_scaler.transform(df[['Score']]).astype(np.float32)


    encoded_Types = type_encoder.transform(df[['Type']])  # transform the column
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
    output = rating_scaler(output)

    output_df = pd.DataFrame(output,columns=['rating'])


    final_df =pd.concat([df['anime_id'], output_df], axis=1)
    final_df=final_df.nlargest(5,'rating')

    anime_ids=final_df['anime_id'].tolist()
    
    # Step 4: Save the top 5 recommended anime for each genre in a new table
    sql_query = """
    INSERT INTO Recommendation (userid, animeid1, animeid2, animeid3, animeid4, animeid5)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
    cursor.execute(sql_query, [user_id] + anime_ids)

    cursor.close()