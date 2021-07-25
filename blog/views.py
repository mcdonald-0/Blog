from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import *
from .models import *
from .decorators import *
from .filters import *

# Create your views here.

def homepage(request):
	blogs = BlogPost.objects.all()

	last_post = blogs.order_by('date_added')[0]
	latest_ten_blogs = blogs.order_by('-date_added')[0:10]

	first_five = latest_ten_blogs[0:5]
	second_five = latest_ten_blogs[5:10]

	blog_filter = BlogPostFilter(request.GET, queryset=blogs)

	context = {
		'last_post': last_post,
		'blogs': blogs,
		'first_five': first_five,
		'second_five': second_five,
		'filter': blog_filter,
	}

	return render(request, 'blog/index.html', context)

# i need to create a featured attribute in my model so it would show featured blogs

@only_logged_in_users
@login_required(login_url='registration:login')
@unregistered_user
def uploadPost(request):
	form = BlogPostForm()
	author = request.user.userprofile

	if request.method == 'POST':
		form = BlogPostForm(request.POST, request.FILES)
		if form.is_valid():
			BlogPost.objects.create(author=author, **form.cleaned_data)
			return redirect('blog:home')
			
	context = {
		'form': form
	}
	return render(request, 'blog/upload_post.html', context)


def viewPost(request, pk):
	blog = BlogPost.objects.get(pk=pk)
	form = CommentForm()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			Comment.objects.create(post=blog, user=request.user.userprofile, **form.cleaned_data)
			return redirect('blog:viewpost', pk=pk)

	context = {
		'blog': blog,
		'form': form,
		'total_likes': blog.total_likes(),
	}

	return render(request, 'blog/view_post.html', context)

@only_logged_in_users
def likePost(request, pk):
	post = get_object_or_404(BlogPost, id=request.POST.get('blog_id'))
	post.likes.add(request.user.userprofile)
	return redirect('blog:viewpost', pk=pk)

@unregistered_user
@login_required(login_url='registration:login')
def updatePost(request, pk):
	blog = BlogPost.objects.get(pk=pk)
	form = BlogPostForm(instance=blog)

	if request.method == 'POST':
		form = BlogPostForm(request.POST, request.FILES, instance=blog)
		if form.is_valid():
			form.save()

			messages.info(request, 'You edited your post!')

			return redirect('blog:viewpost', pk=pk)

	context = {
		'form': form,
		'blog': blog
    }

	return render(request, 'blog/update_post.html', context)

@restriction_of_delete_from_unauthenticated_user
@restriction_of_delete
def deletePost(request, pk):
	item = BlogPost.objects.get(pk=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('blog:home')

	context = {
		'item': item,
    }

	return render(request, 'blog/delete_post.html', context)

@only_logged_in_users
@login_required(login_url='registration:login')
def viewMyProfile(request):
	user = request.user.userprofile
	user_posts = user.blogpost_set.all()

	user_details = UserProfile.objects.get(id=user.id)

	context = {
		'user': user,
		'user_posts': user_posts,
		'user_details': user_details,
	}
	return render(request, 'blog/self_profile_view.html', context)


def viewOtherProfile(request, pk):
	user = get_object_or_404(UserProfile, pk=pk)

	context = {
		'user': user
	}
	return render(request, 'blog/user_profile_view.html', context)
# i would download some template to render a user details and then the blogs they have posted

@only_logged_in_users
@login_required(login_url='registration:login')
def editProfile(request):
	user = request.user.userprofile
	form = EditProfileForm(instance=user)

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('blog:viewmyprofile') 

	context = {
		'form': form
	}
	return render(request, 'blog/user_profile_settings.html', context)

def search(request):
	blogs = BlogPost.objects.all()
	users = UserProfile.objects.all()

	blog_filter = BlogPostFilter(request.GET, queryset=blogs)

	blogs = blog_filter.qs

	context = {
		'filter': blog_filter,
		'blogs': blogs,
	}

	return render(request, 'blog/search.html', context)

def category(request, category):
	category = Category.objects.get(name=category)
	blog_related_by_category = get_list_or_404(BlogPost, category=category)

	context = {
		'blogs': blog_related_by_category,
	}

	return render(request, 'blog/categories.html', context)