from django.shortcuts import render, redirect
from .models import Anime,User
from .forms import AddToWishlistForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    anime_list = Anime.objects.all()
    selected_score = request.POST.get('score')  # Get the selected score from the form submission
    print("Selected score:", selected_score)  # Debug print
    if selected_score:  # Check if a score value is provided
        min_score = float(selected_score)
        max_score = min_score + 0.99  # Determine the maximum score based on the selected whole number
        anime_list = anime_list.filter(score__gte=min_score, score__lt=max_score)
    return render(request, 'WL/index.html', {'anime_list': anime_list})

def empty_cart(request):
    if 'cart' in request.session:
        del request.session['cart'] 
    previous_url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(previous_url)

# views.py

def add_to_wishlist(request, anime_id):  # Ensure the view accepts anime_id
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST, initial={'anime_id': anime_id})  # Pass anime_id as initial data
        if form.is_valid():
            # Rest of the view code

            
            wishlist = request.session.get('wishlist', [])
            if anime_id not in wishlist:
                wishlist.append(anime_id)
                request.session['wishlist'] = wishlist
                print('Added anime with ID:', anime_id, 'to wishlist')
                messages.info(request, 'Anime added to wishlist')
                print('Number of items in wishlist:', len(wishlist))
            else:
                # Add a message if the item is already in the wishlist
                messages.info(request, 'Anime already in wishlist')
               
    return redirect('wishlist')

def view_wishlist(request):
    # Retrieve the wishlist items from the session
    wishlist = request.session.get('wishlist', [])
    
    # Retrieve the anime items in the wishlist based on their IDs
    anime_items_in_wishlist = Anime.objects.filter(anime_id__in=wishlist)
    
    # Pass the anime items to the template context
    return render(request, 'WL/wishlist.html', {'anime_items_in_wishlist': anime_items_in_wishlist})


# views.py

from django.shortcuts import redirect

def remove_from_wishlist(request, anime_id):
    if request.method == 'POST':
        wishlist = request.session.get('wishlist', [])
        if anime_id in wishlist:
            wishlist.remove(anime_id)
            request.session['wishlist'] = wishlist
            # Optionally, you can add a message here indicating successful removal
            return redirect('wishlist')  # Redirect back to the wishlist page
    # If the request method is not POST or the anime is not in the wishlist, redirect back to the wishlist page
    return redirect('wishlist')
