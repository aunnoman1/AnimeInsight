from django.shortcuts import render, redirect
from .models import Anime
from .forms import AddToCartForm
from django.urls import reverse
from django.http import HttpResponseRedirect
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

from django.contrib import messages

def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            anime_id = form.cleaned_data['anime_id']
            
            cart = request.session.get('cart', [])
            if anime_id not in cart:
                cart.append(anime_id)
                request.session['cart'] = cart
                print('Added anime with ID:', anime_id, 'to cart')
                messages.info(request, 'Product Added')
                print('Number of items in cart:', len(cart))
            else:
                # Add a message if the item is already in the cart
                messages.info(request, 'Product already in cart')
               
    return redirect('anime_list')

def view_cart(request):
    # Retrieve the cart items from the session
    cart = request.session.get('cart', [])
    
    # Retrieve the anime items in the cart based on their IDs
    anime_items_in_cart = Anime.objects.filter(mal_id__in=cart)
    
    # Render the cart template with the anime items in the cart
    return render(request, 'WL/cart.html', {'anime_items_in_cart': anime_items_in_cart})