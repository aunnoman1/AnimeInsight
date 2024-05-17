from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.db import connection,IntegrityError
from django.conf import settings
from .models import User, FavGenres, Profile, Wishlist, AnimeMetadata,Historywatch
from django.contrib import messages
import logging
import os

import numpy as np
import pandas as pd
import tensorflow as tf
from joblib import load
import threading
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

@tf.keras.utils.register_keras_serializable()
def split_func(input_str):
    return tf.strings.split(input_str, sep=", ")


def index(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
             SELECT  Top 300 * FROM Anime_Metadata
    WHERE Score >7.99
    order by Score desc
            '''
        )
        anime_list = dictfetchall(cursor)
        

    selected_score = request.POST.get('score')
    if selected_score:
        min_score = float(selected_score)
        max_score = min_score + 0.99
        # Filter the fetched objects based on the selected score
        anime_list = [anime for anime in anime_list if min_score <= anime['score'] < max_score]

    return render(request, 'AnimeInsightApp/index.html', {'anime_list': anime_list})


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
# Views for managing anime wishlist


@login_required
def view_wishlist(request):
    # Fetch the current user instance from the request
    user_instance = request.user
    
    # Execute raw SQL query to fetch wishlist items for the current user
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                w.userid,
                a.anime_id,
                a.name,
                a.image_url,
                a.score
                
            FROM wishlist w
            INNER JOIN Anime_Metadata a ON w.animeid = a.anime_id
            WHERE w.userid = %s
        """, [user_instance.id])
        wishlist = cursor.fetchall()
    
    return render(request, 'AnimeInsightApp/wishlist.html', {'wishlist': wishlist})



@login_required
def remove_from_wishlist(request, anime_id):
    if request.method == 'POST':
        
        user_instance = request.user

        # Execute raw SQL query to delete the wishlist item
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM wishlist WHERE userid = %s AND animeid = %s", [user_instance.id, anime_id])
            rows_deleted = cursor.rowcount

        if rows_deleted > 0:
            messages.success(request, 'Anime removed from wishlist')
        else:
            messages.error(request, 'Anime not found in wishlist')
    return redirect('AnimeInsightApp:wishlist')
#-------------------------------
@login_required
def add_to_history(request, anime_id):
    if request.method == 'POST':
        user_instance = request.user
        
        anime_id = int(anime_id)
        
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) FROM historywatch 
                WHERE userid = %s AND animeid = %s
            """, [user_instance.id, anime_id])
            row_count = cursor.fetchone()[0]

            if row_count == 0:
                cursor.execute("""
                    INSERT INTO historywatch (userid, animeid)
                    VALUES (%s, %s)
                """, [user_instance.id, anime_id])
                messages.success(request, 'Anime added to history')
                
                t = threading.Thread(target=recommend_anime, args=[request])
                t.start()
            else:
                messages.info(request, 'Anime already in history')
    
    return redirect('AnimeInsightApp:index')
#---------------------------#
@login_required
def view_history(request):
    user_instance = request.user
    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                h.userid,
                a.anime_id,
                a.name,
                a.image_url,
                a.aired,
                a.score
            FROM historywatch h
            INNER JOIN Anime_Metadata a ON h.animeid = a.anime_id
            WHERE h.userid = %s
        """, [user_instance.id])
        history = cursor.fetchall()
    
    return render(request, 'AnimeInsightApp/history.html', {'history': history})


@login_required
def clear_history(request):
    user_instance = request.user

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Historywatch WHERE userid = %s", [user_instance.id])

    messages.success(request, 'Watch history cleared successfully.')

    return redirect('AnimeInsightApp:view_history')

# Other views...

@login_required
def add_to_wishlist(request, anime_id):
    if request.method == 'POST':
        user_instance = request.user

        anime_id = int(anime_id)
        
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) FROM wishlist 
                WHERE userid = %s AND Animeid = %s
            """, [user_instance.id, anime_id])
            row_count = cursor.fetchone()[0]

            if row_count == 0:
                cursor.execute("""
                    INSERT INTO wishlist (userid, animeid)
                    VALUES (%s, %s)
                """, [user_instance.id, anime_id])
                messages.success(request, 'Anime added to wishlist')
            else:
                messages.info(request, 'Anime already in wishlist')

    return redirect('AnimeInsightApp:index')
	
	
	
	














# Create your views here.

@login_required
def home(request):
    context={}
    if request.method=='GET':
        cursor = connection.cursor()
        context['animes']=[]
        cursor.execute("select AnimeID1 , AnimeID2 , AnimeID3 , AnimeID4 , AnimeID5 , AnimeID6 , AnimeID7 , AnimeID8 , AnimeID9 , AnimeID10  from recommendation where userID = %s",[request.user.id])
        animeids=cursor.fetchone()
        if isinstance(animeids,tuple):
            for animeid in animeids:
                cursor.execute("SELECT anime_id , Name , Image_URL FROM anime_metadata WHERE anime_id = %s",[animeid])
                animeinfo=cursor.fetchone()
                context['animes'].append(animeinfo)


        
        return render(request, 'AnimeInsightApp/Home.html',context=context)
    
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
        gender= request.POST['gender']
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
        profile.gender=gender
        profile.save()
        t= threading.Thread(target=recommend_anime,args=[request])
        t.start()
        return redirect('AnimeInsightApp:home')


    else:
        context['genres']=[g[0] for g in FavGenres.genre.field.choices]
        context['genders']=[g[1] for g in Profile.gender.field.choices]
        return render(request,'AnimeInsightApp/complete_profile.html',context)
    

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('AnimeInsightApp:login_request')



def get_embedding(anime_id):
    cursor=connection.cursor()
    cursor.execute("SELECT tensor_1 , tensor_2, tensor_3,tensor_4 , tensor_5, tensor_6,tensor_7 , tensor_8, tensor_9,tensor_10 , tensor_11, tensor_12,tensor_13 , tensor_14, tensor_15, tensor_16 FROM anime_tensors WHERE animeid = %s", [anime_id])
    row = cursor.fetchone()
    cursor.close()
    if row:
        return np.array(row)
    else:
        return None

# Define function to find similar anime embeddings
def find_similar_anime(anime_id, top_n=5):
    # Retrieve the embedding of the given anime ID
    query_embedding = get_embedding(anime_id)
    if query_embedding is None:
        print("Anime ID not found")
        return
    
    # Retrieve all embeddings from the database
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM anime_tensors where animeid != %s",[anime_id])
    embeddings = []
    anime_ids = []
    for row in cursor.fetchall():
        anime_ids.append(row[0])
        embeddings.append(row[1:])
    
    # Compute cosine similarity between query_embedding and all other embeddings
    similarities = cosine_similarity([query_embedding], embeddings)
    
    # Sort the results based on similarity
    sorted_indices = np.argsort(similarities[0])[::-1]
    
    # Retrieve top N similar anime
    top_n_similar = [anime_ids[idx] for idx in sorted_indices[:top_n]]
    
    return top_n_similar


def recommend_anime(request):
    user_id=request.user.id
    user_mean_score= 8.0
    
    cursor = connection.cursor()
    # Step 1: Retrieve the user's details
    cursor.execute("SELECT genre FROM AnimeInsightApp_favgenres WHERE userid_id = %s", [user_id])
    fav_genres = cursor.fetchall()

    cursor.execute("SELECT gender,dob from AnimeInsightApp_profile WHERE userid_id = %s", [user_id])
    fetched= cursor.fetchone()
    user_gender=fetched[0]
    dob=fetched[1]
    user_age = (datetime.now().date() - dob).days // 365
    user_df=pd.DataFrame([[user_gender,user_mean_score,user_age]],columns=['Gender','Mean Score','age'])

    # Step 2: Get the top 50 anime for each genre from the animemetadata table
    anime_list = []
    
    cursor.execute('select animeid from historywatch where userid = %s',[request.user.id])
    watched_animes=cursor.fetchall()
    watched_animes=[watched_anime[0] for watched_anime in watched_animes]
    if len(watched_animes) < 3:
        for fav_genre in fav_genres:
            cursor.execute("""
                SELECT top 2000 anime_id, Score,	Genres,	Type , Studios , Source
                FROM Anime_Metadata
                WHERE Genres LIKE %s
                order by Score DESC
            """, ['%' + fav_genre[0] + '%'])
            anime_list.extend(cursor.fetchall())

    for watched_anime in watched_animes:
        similar_animes=find_similar_anime(watched_anime,2000)
        for similar_anime in similar_animes:
            cursor.execute("""
                SELECT anime_id, Score,	Genres,	Type , Studios , Source
                FROM Anime_Metadata
                WHERE anime_id = %s
            """, [similar_anime])
            anime_list.append(cursor.fetchone())
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(np.array(anime_list), columns=columns)
    df.drop_duplicates(inplace=True)
    df=df[~df['anime_id'].isin(watched_animes)]
    df=df[~(df['Type']=='Music')]

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

    

    studio_vectorize_layer_model=tf.keras.models.load_model(preprocesing_path+'/studio_vectorize_layer_model')
    studio_vectorize_layer = studio_vectorize_layer_model.layers[0]
    num_studios=len(studio_vectorize_layer.get_vocabulary())
    genre_vectorize_layer_model=tf.keras.models.load_model(preprocesing_path+'/genre_vectorize_layer_model')
    genre_vectorize_layer = genre_vectorize_layer_model.layers[0]
    num_genres=len(genre_vectorize_layer.get_vocabulary())
    source_vectorize_layer_model=tf.keras.models.load_model(preprocesing_path+'/source_vectorize_layer_model')
    source_vectorize_layer = source_vectorize_layer_model.layers[0]
    num_sources=len(source_vectorize_layer.get_vocabulary())

    
    df.fillna({'Score':df['Score'].astype(np.float32).mean()},inplace=True)

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


    encoded_gender = gender_encoder.transform(user_df[['Gender']])  # Fit and transform the column
    encoded_df = pd.DataFrame(encoded_gender.toarray(), columns=gender_encoder.categories_[0])  # Create a DataFrame from the encoded columns

    user_df=pd.concat([user_df, encoded_df], axis=1)  # Concatenate the original DataFrame with the encoded DataFrame
    user_df.drop(['Gender'],axis=1,inplace=True)

    user_df.loc[:,'Mean Score']=mean_score_scaler.transform(user_df[['Mean Score']])

    user_df=user_df.reindex(user_df.index.repeat(df.shape[0]))

    user_input=user_df.to_numpy()


    anime_columns=df.iloc[:,1:1+anime_input_shape].to_numpy(dtype='float32')
    anime_studio_embedding_columns = df.iloc[:,1+anime_input_shape:1+anime_input_shape+studio_max_length].to_numpy()
    anime_genre_embedding_columns= df.iloc[:,1+anime_input_shape+studio_max_length:1+anime_input_shape+studio_max_length+genre_max_length].to_numpy()
    anime_source_embedding_columns = df.iloc[:,-1:].to_numpy()


    input={'user_input':user_input, 'anime_input':anime_columns,'anime_genre_embedding_input':anime_genre_embedding_columns,'anime_studio_embedding_input':anime_studio_embedding_columns,'anime_source_embedding_input':anime_source_embedding_columns}
    
    output=model(input)
    output = rating_scaler.inverse_transform(output)

    output_df = pd.DataFrame(output,columns=['rating'],index=df.index)


    final_df =pd.concat([df['anime_id'], output_df], axis=1)
    final_df=final_df.nlargest(10,'rating')

    anime_ids=final_df['anime_id'].tolist()
    
    # Step 4: Save the top 5 recommended anime for each genre in a new table
    sql_query = """

    if exists(select * from recommendation where userid=%s)
    begin
        update recommendation
        set AnimeID1=%s,AnimeID2=%s,AnimeID3=%s,AnimeID4=%s,AnimeID5=%s,AnimeID6=%s,AnimeID7=%s,AnimeID8=%s,AnimeID9=%s,AnimeID10=%s
        where userid=%s
    end
    else
    begin
        insert into recommendation
        values
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    end
    """
    cursor.execute(sql_query, [user_id]+anime_ids+[user_id]+[user_id]+anime_ids)

    cursor.close()
    
    
def search(request):
    context={}
    context['animes']=[]
    search_str=request.GET.get("q")
    search_term='%'+search_str+'%'
    cursor=connection.cursor()
    cursor.execute("""
                    select anime_id,[Name],English_name,Image_URL
                    from Anime_Metadata
                    where (Name like %s or English_name like %s ) and Genres not like '%%Hentai%%'  and Genres not like '%%Ecchi%%'
                   """,[search_term,search_term])
    results=cursor.fetchall()
    if isinstance(results,list):
        for result in results:
            if(result[1]!=None and result[2]!=None):
                name=result[1]+'('+result[2]+')'
            elif(result[1]==None):
                name=result[2]
            else:
                name=result[1]
            id=result[0]
            image_url=result[3]
            animeinfo=[id,name,image_url]
            context['animes'].append(animeinfo)
    
    return render(request, 'AnimeInsightApp/search.html',context=context)
    
    
def about_us(request):
    return render(request,'AnimeInsightApp/about_us.html')
    
    
    
    
    
#---------------------------------

def filter_by_genre(request):
    selected_genre = request.POST.get('genre')
    if isinstance(selected_genre,str):
        selected_genre='%'+selected_genre+'%'
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT Top 1000 * FROM Anime_Metadata
            where genres like %s
            order by Score desc
            ''',[selected_genre]
        )
        anime_list = dictfetchall(cursor)

    # if selected_genre:
    #     # Filter the fetched objects based on the selected genre
    #     anime_list = [anime for anime in anime_list if anime['Genres'] and selected_genre in anime['Genres']]

    # Extract the first genre from each row to populate the filter options
    genres = [g[0] for g in FavGenres.genre.field.choices]

    return render(request, 'AnimeInsightApp/Genre.html', {'anime_list': anime_list, 'genres': sorted(genres)})
		
def request_anime(request):
    if request.method == 'POST':
        name=request.POST['name']
        cursor=connection.cursor()
        cursor.execute('insert into request values (%s,%s)',[request.user.id,name])
        cursor.close()
        return redirect('AnimeInsightApp:request_anime')
    return render(request, 'AnimeInsightApp/request_anime.html')


def one_anime_page(request, anime_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Anime_Metadata WHERE anime_id = %s", [anime_id])
        anime = cursor.fetchone()
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT rev,rate FROM Review_Rating WHERE anime_id = %s", [anime_id])
        reviews = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute("SELECT username FROM AnimeInsightApp_user join Review_Rating on Review_Rating.user_id=AnimeInsightApp_user.id where anime_id = %s", [anime_id])
        usr = cursor.fetchall()

    
    similar_animes=find_similar_anime(anime_id,5)
    animes=[]
    with connection.cursor() as cursor:
        for similar_anime in similar_animes:
            cursor.execute("SELECT anime_id , Name , Image_URL FROM anime_metadata WHERE anime_id = %s",[similar_anime])
            animeinfo=cursor.fetchone()
            animes.append(animeinfo)

    
    return render(request, 'AnimeInsightApp/oneanimepage.html', {'anime': anime, 'reviews': reviews, 'usr':usr,'animes':animes})
    


def add_review(request, anime_id):
    if request.method == 'POST':
        user_instance = request.user
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM Review_Rating WHERE user_id = %s AND anime_id = %s", [user_instance.id, anime_id])
            review_count = cursor.fetchone()[0]
        if review_count > 0:
            with connection.cursor() as cursor:
                sql_query = """
                    UPDATE Review_Rating
                    SET rev = %s, rate = %s
                    WHERE user_id = %s AND anime_id = %s;
                """
                cursor.execute(sql_query, [review_text, rating, user_instance.id, anime_id])
        else:
            with connection.cursor() as cursor:
                sql_query = """
                    INSERT INTO Review_Rating (user_id, anime_id, rev, rate)
                    VALUES (%s, %s, %s, %s);
                """
                cursor.execute(sql_query, [user_instance.id, anime_id, review_text, rating])
        return redirect('AnimeInsightApp:one_anime_page',anime_id)