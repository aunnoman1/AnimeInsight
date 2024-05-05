from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AnimeMetadata, Wishlist

def index(request):
    anime_list = AnimeMetadata.objects.all()
    selected_score = request.POST.get('score')
    print("Selected score:", selected_score)
    if selected_score:
        min_score = float(selected_score)
        max_score = min_score + 0.99
        anime_list = anime_list.filter(score__gte=min_score, score__lt=max_score)
    return render(request, 'AnimeInsightApp/index.html', {'anime_list': anime_list})

from django.contrib.auth.models import User  # Import the User model

def add_to_wishlist(request, anime_id):
    if request.method == 'POST':
        # Fetch the current user instance based on username
        username = 'admin'  # Replace 'admin' with the appropriate username
        user_instance = User.objects.get(username=username)
        
        # Get the anime ID from the request
        anime_id = int(request.POST.get('anime_id'))
        
        # Check if the anime is already in the user's wishlist
        if not Wishlist.objects.filter(userid=user_instance, animeid_id=anime_id).exists():
            # If not, add it to the wishlist
            Wishlist.objects.create(userid=user_instance, animeid_id=anime_id)
            messages.success(request, 'Anime added to wishlist')
        else:
            # If it's already in the wishlist, display a message
            messages.info(request, 'Anime already in wishlist')
    
    # Redirect to the index page after adding the anime to the wishlist
    return redirect('index')


def view_wishlist(request):
    # Fetch the current user instance based on username
    username = 'admin'  # Replace 'admin' with the appropriate username
    user_instance = User.objects.get(username=username)
    
    wishlist = Wishlist.objects.filter(userid=user_instance)
    return render(request, 'AnimeInsightApp/wishlist.html', {'wishlist': wishlist})


def remove_from_wishlist(request, anime_id):
    if request.method == 'POST':
        # Fetch the current user instance based on username
        username = 'admin'  # Replace 'admin' with the appropriate username
        user_instance = User.objects.get(username=username)
        
        wishlist_item = Wishlist.objects.filter(userid=user_instance, animeid_id=anime_id)
        if wishlist_item.exists():
            wishlist_item.delete()
            messages.success(request, 'Anime removed from wishlist')
        else:
            messages.error(request, 'Anime not found in wishlist')
    return redirect('wishlist')







##-------------------------------------------------------------------------------
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from .models import User,FavGenres,Profile
import logging

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
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        # Check if user already exists
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            context['message'] = "User already exists"
            return render(request, "AnimeInsightApp/registration.html", context)

        # Password validation
        if password != password2:
            context['message'] = "Passwords do not match"
            return render(request, "AnimeInsightApp/registration.html", context)

        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)

        # Create profile
        profile = Profile.objects.create(userid=user)

        # Log in the user
        login(request, user)
        
        return redirect("AnimeInsightApp:complete_profile")
    
    return render(request, "AnimeInsightApp/registration.html", context)
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
