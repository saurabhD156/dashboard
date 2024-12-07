from django.shortcuts import render
from .models import Category, Tag, Post


# Create your views here.

def home(request):

    context = {
        'title' : 'Dashboard'
    }
    return render(request, 'dashboard.html', context)


# -- ========  Caategory ======= ---
def category(request):

    category = Category.objects.all()
    category_count = category.count()

    context = {
        'title' : 'Categories',
        'category' : category,
        'category_count' : category_count
    }
    return render(request, 'categories.html', context)

def add_category(request):

    context= {
        'title' : "Add category"
    }
    return render(request, 'add-category.html', context)


# -- ========  Post ======= ---
def post_list(request):

    context = {
        'title'         : 'Post List',
    }
    return render(request, 'post-list.html', context)

def post_create(request):

    context = {
        'title' : 'Post Create'
    }
    return render(request, 'post-create.html', context)

def post_edit(request):

    context = {
        'title' : 'Post Edit'
    }
    return render(request, 'post-edit.html', context)


# -- ========  Author ======= ---
def author_list(request):

    context = {
        'title' : 'Author List'
    }
    return render(request, 'author-list.html', context)

def author_single(request):

    context = {
        'title' : 'Author Single'
    }
    return render(request, 'author-single.html', context)

def edit_profile(request):

    context = {
        'title' : 'Edit Profile'
    }
    return render(request, 'edit-profile.html', context)


# -- ========  Additional ======= ---
def reviews(request):

    context = {
        'title' : 'Reviews'
    }
    return render(request, 'reviews.html', context)

def settings(request):

    context = {
        'title' : 'Settings'
    }
    return render(request, 'settings.html', context)

