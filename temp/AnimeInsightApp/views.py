from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, FavGenres, Profile, Wishlist, AnimeMetadata,Historywatch
from django.contrib import messages
import logging
from django.db import connection

logger = logging.getLogger(__name__)
def index(request):
    # Fetch all anime metadata objects limited to the first 100 elements
    anime_list = AnimeMetadata.objects.all()[:100]

    selected_score = request.POST.get('score')
    if selected_score:
        min_score = float(selected_score)
        max_score = min_score + 0.99
        # Filter the fetched objects based on the selected score
        anime_list = anime_list.filter(score__gte=min_score, score__lt=max_score)

    return render(request, 'AnimeInsightApp/index.html', {'anime_list': anime_list})
# Views for managing anime wishlist
@login_required
@login_required
def add_to_wishlist(request, anime_id):
    if request.method == 'POST':
        # Fetch the current user instance from the request
        user_instance = request.user
        
        # Get the anime ID from the URL parameter
        anime_id = int(anime_id)
        
        # Check if the anime is already in the user's wishlist
        if not Wishlist.objects.filter(userid=user_instance, animeid_id=anime_id).exists():
            # If not, add it to the wishlist
            Wishlist.objects.create(userid=user_instance, animeid_id=anime_id)
            messages.success(request, 'Anime added to wishlist')
        else:
            # If it's already in the wishlist, display a message
            messages.info(request, 'Anime already in wishlist')
    
    # Redirect to the index page after adding the anime to the wishlist
    return redirect('AnimeInsightApp:index')

@login_required
def view_wishlist(request):
    # Fetch the current user instance from the request
    user_instance = request.user
    
    wishlist = Wishlist.objects.filter(userid=user_instance)
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

#----
@login_required
def add_to_history(request, anime_id):
    if request.method == 'POST':
        # Fetch the current user instance from the request
        user_instance = request.user
        
        # Get the anime ID from the URL parameter
        anime_id = int(anime_id)
        
        # Check if the anime is already in the user's history
        if not Historywatch.objects.filter(userid=user_instance, animeid_id=anime_id).exists():
            # If not, add it to the history
            Historywatch.objects.create(userid=user_instance, animeid_id=anime_id)
            messages.success(request, 'Anime added to history')
        else:
            # If it's already in the history, display a message
            messages.info(request, 'Anime already in history')
    
    # Redirect to the index page after adding the anime to the history
    return redirect('AnimeInsightApp:index')
def view_history(request):
    # Fetch the current user instance from the request
    user_instance = request.user
    
    # Retrieve the watch history for the current user
    history = Historywatch.objects.filter(userid=user_instance)
    
    # Render the history template with the retrieved history data
    return render(request, 'AnimeInsightApp/history.html', {'history': history})
# Other views...


@login_required
def home(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'AnimeInsightApp/Home.html')

def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(userid=user)
            if profile.registered:
                return redirect("AnimeInsightApp:home")
            else:
                return redirect('AnimeInsightApp:complete_profile')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'AnimeInsightApp/login.html', context)
    else:
        return render(request, 'AnimeInsightApp/login.html', context)

def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user_exists = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exists = True
            context['message'] = "User already exists"
        except:
            # If not, log that this is a new user
            logger.debug("{} is a new user".format(username))
        if password != password2:
            context['message'] = "Passwords do not match"
            return render(request, "AnimeInsightApp/registration.html", context)

        # If it is a new user
        if not user_exists:
            user = User.objects.create_user(username=username, password=password, email=email)
            profile = Profile(userid=user)
            profile.save()
            login(request, user)
            return redirect("AnimeInsightApp:complete_profile")
        else:
            return render(request, 'AnimeInsightApp/registration.html', context)
    else:
        return render(request, 'AnimeInsightApp/registration.html', context)

@login_required
def complete_profile(request):
    context = {}
    if request.method == "POST":
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
        profile.dob = date_of_birth
        profile.registered = True
        profile.save()

        return redirect('AnimeInsightApp:home')
    else:
        context['genres'] = [g[0] for g in FavGenres.genre.field.choices]
        return render(request, 'AnimeInsightApp/complete_profile.html', context)

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('AnimeInsightApp:login_request')
