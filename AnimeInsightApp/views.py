from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from .models import User,FavGenres
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
            return redirect("AnimeInsightApp:home")
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
            login(request,user)
            return redirect("AnimeInsightApp:home")
        else:
            return render(request,'AnimeInsightApp/registration.html',context)
    else:
        return render(request,'AnimeInsightApp/registration.html',context)
        
def complete_profile(request):
    context={}
    if request.method=="POST":
        pass
    else:
        context['genres']=[g[0] for g in FavGenres.GENRE_CHOICES]
        return render(request,'AnimeInsightApp/complete_profile.html')

        
