from django.urls import path
from . import views

# urls starts from here ...

urlpatterns = [
    path('', views.home, name='home'),

    # --- ==========  Category  ========== ------
    path('category/', views.category, name='category'),
    path('add-category/', views.add_category, name='add_category'),

    # --- ==========  Post  ========== ------ 
    path('post-list/', views.post_list, name='post_list'),
    path('post-create/', views.post_create, name='post_create'),
    path('post-edit/', views.post_edit, name='post_edit'),

    # --- ==========  Author  ========== ------ 
    path('author-list/', views.author_list, name='author_list'),
    path('author-single/', views.author_single, name='author_single'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),    

    # --- ==========  Additional  ========== ------
    path('reviews/', views.reviews, name='reviews'),    
    path('settings/', views.settings, name='settings'),
    path('images/', views.images, name='images'),

]
