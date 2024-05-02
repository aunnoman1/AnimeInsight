from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    if request.method=='GET':
        return render(request, 'AnimeInsightApp/Home.html')
