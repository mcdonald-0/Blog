from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('signup/', views.user_signup, name='signup'),
]
