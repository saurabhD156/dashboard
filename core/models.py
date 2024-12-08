from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    original_image  = models.ImageField(upload_to='images/', max_length=2000, blank=False, null=False)
    medium_image    = models.ImageField(upload_to='images/', max_length=900, blank=False, null=False)
    small_image     = models.ImageField(upload_to='images/', max_length=300, blank=False, null=False)
    alt_tag         = models.CharField(max_length=250, blank=True, null=True)
    title           = models.CharField(max_length=250, blank=True, null=True)
    description     = models.TextField(max_length=250, blank=True, null=True)
    fileName        = models.CharField(max_length=250, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MetaData(models.Model):
    title           = models.TextField(max_length=250)
    description     = models.TextField(max_length=250)
    keywords        = models.CharField(max_length=250)
    featured_image  = models.ForeignKey(Image, on_delete=models.CASCADE)
    index           = models.CharField(max_length=250)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    Name            = models.CharField(max_length=250)
    description     = models.TextField(max_length=250)
    images          = models.ForeignKey(Image, on_delete=models.CASCADE)
    slug            = models.SlugField(unique=True)
    metadata        = models.OneToOneField(MetaData, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    name            = models.CharField(max_length=250)
    slug            = models.SlugField(unique=True)
    metadata        = models.ManyToManyField(MetaData)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title               = models.CharField(max_length=250)
    short_description   = models.TextField(max_length=250)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    content             = models.TextField()
    comments            = models.TextField(max_length=500)
    views               = models.PositiveIntegerField()
    slug                = models.SlugField(unique=True)
    published           = models.BooleanField(default=False)
    featured_image      = models.ForeignKey(Image, on_delete=models.CASCADE, blank=False, null=False)
    tags                = models.ManyToManyField(Tag, related_name='posts', blank=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name='posts', blank=True)
    metadata            = models.OneToOneField(MetaData, on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True, blank= True, null=True)
    updated_at          = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
