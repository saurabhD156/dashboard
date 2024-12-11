from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Tag, Post, Image


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
    return render(request, 'category/categories.html', context)

def add_category(request):

    context= {
        'title' : "Add category"
    }
    return render(request, 'category/add-category.html', context)


# -- ========  Post ======= ---
def post_list(request):

    posts = Post.objects.all()
    posts_count = posts.count()
    featured_image_count = Post.objects.filter(featured_image__isnull=False).count()

    context = {
        'title'         : 'Post List',
        'posts'         : posts,
        'posts_count'   : posts_count,
        'featured_image_count' : featured_image_count
    }
    return render(request, 'post/post-list.html', context)

def post_create(request):

    context = {
        'title' : 'Post Create'
    }
    return render(request, 'post/post-create.html', context)

def post_edit(request):

    context = {
        'title' : 'Post Edit'
    }
    return render(request, 'post/post-edit.html', context)


# -- ========  Author ======= ---
def author_list(request):

    context = {
        'title' : 'Author List'
    }
    return render(request, 'author/author-list.html', context)

def author_single(request):

    context = {
        'title' : 'Author Single'
    }
    return render(request, 'author/author-single.html', context)

def edit_profile(request):

    context = {
        'title' : 'Edit Profile'
    }
    return render(request, 'author/edit-profile.html', context)


# -- ========  Additional ======= ---
def reviews(request):

    context = {
        'title' : 'Reviews'
    }
    return render(request, 'additional/reviews.html', context)

def settings(request):

    context = {
        'title' : 'Settings'
    }
    return render(request, 'additional/settings.html', context)

def images(request):
    if request.method == 'POST':
        # Collect data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        alt_tag = request.POST.get('alt_tag')
        file_name = request.POST.get('file_name')
        
        # Handle uploaded files
        original_image = request.FILES.get('original_image')
        medium_image = request.FILES.get('medium_image')
        small_image = request.FILES.get('small_image')

        # Create a new Image object
        try:
            new_image = Image.objects.create(
                original_image=original_image,
                medium_image=medium_image,
                small_image=small_image,
                alt_tag=alt_tag,
                title=title,
                description=description,
                fileName=file_name,
            )
            new_image.save()
            messages.success(request, "Image added successfully!")
        except Exception as e:
            messages.error(request, f"Error adding image: {e}")

        return redirect('images')  

    # GET request to display existing images
    images = Image.objects.all()
    context = {
        'title': 'Images',
        'images': images,
    }
    return render(request, 'images.html', context)