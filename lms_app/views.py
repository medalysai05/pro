from django.shortcuts import render
from .models import Category, Book
from .forms import BookForm , CategoryForm

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
         
        add_cat =  CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            # Rediriger l'utilisateur ou faire toute autre action nécessaire
    else:
        form = BookForm()
    
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': form,
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

#from .models import *   categories = Category.objects.all()