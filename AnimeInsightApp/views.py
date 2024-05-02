from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

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
    pass
