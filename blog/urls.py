from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homepage, name='home'),

    path('upload/', views.uploadPost, name='uploadpost'),

    path('view/<str:pk>/', views.viewPost, name="viewpost"),
    path('update/<str:pk>/', views.updatePost, name="updatepost"),
    path('remove/<str:pk>/', views.deletePost, name="deletepost"),

    path('profile/', views.viewMyProfile, name='viewmyprofile'),
    path('profile/settings/', views.editProfile, name='editprofile'),
    path('profile/view/<str:pk>/', views.viewOtherProfile, name='viewotherprofile'),
]
