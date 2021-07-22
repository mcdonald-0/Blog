from django.http import HttpResponse

from django.shortcuts import redirect

from django.contrib import messages

from .models import *


def unregistered_user(view_func):
	def wrapper(request, *args, **kwargs):
        
		if request.user.userprofile.first_name == None:
			messages.info(request, 'Dear %s you need to add some details about you!' % request.user)

			return redirect('blog:editprofile')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper

def restriction_of_delete(view_func):
	def wrapper(request, pk):

		item = BlogPost.objects.get(pk=pk)

		if request.user.userprofile != item.author:
			return HttpResponse('<h1>You are not authorized to view this page!</h1>')
		else:
			return view_func(request, pk)

	return wrapper


def restriction_of_delete_from_unauthenticated_user(view_func):
	def wrapper(request, pk):

		if request.user.is_authenticated == False:
			return HttpResponse('<h1>You are not logged on!</h1>')
		else:
			return view_func(request, pk)
		
	return wrapper


def only_logged_in_users(view_func):
	def wrapper(request, *args, **kwargs):

		if request.user.is_authenticated:
			return view_func(request, *args, **kwargs)
		else:
			messages.warning(request, 'You Have To Login In Order To Perform That Action!')
			return redirect('registration:login')

	return wrapper