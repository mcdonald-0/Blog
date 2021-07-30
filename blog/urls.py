from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', homepage, name='home'),

    path('search/', search, name='search'),

    path('upload/', uploadPost, name='uploadpost'),

    path('category/', category, name='category'),
    path('category/<str:category>/', categoryDetail, name='categorydetial'),

    path('view/<str:pk>/', viewPost, name="viewpost"),
    path('like/<str:pk>/', likePost, name="likepost"),
    path('update/<str:pk>/', updatePost, name="updatepost"),
    path('remove/<str:pk>/', deletePost, name="deletepost"),

    path('profile/', viewMyProfile, name='viewmyprofile'),
    path('profile/settings/', editProfile, name='editprofile'),
    path('profile/view/<str:pk>/', viewOtherProfile, name='viewotherprofile'),
]
