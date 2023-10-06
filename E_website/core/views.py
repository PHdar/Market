from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import SignupForm
from django.contrib.auth import logout

def index(request):
    item = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html' , 
    {
        'categories' : categories,
        'item' : item,
    })

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })

def logout_uer(request):
    logout(request)
    return redirect('/login/')
