from django.db import models

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    birthdate = models.DateField(null=True)

    GENDER_CHOICES = (
    		('M', 'Male'),
    		('F', 'Female'),
    	)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    profile_picture = models.ImageField(default='blog.jpg', null=True)

    bio = models.TextField(null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=200, null=True)
    related_image = models.ImageField(default='blog.jpg', upload_to="blog_images/", null=True)
    content = RichTextField()
 
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(UserProfile, related_name='likes', blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return "%s | %s " % (self.title, self.author)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)

    post = models.ForeignKey(BlogPost, null=True, related_name="comments", on_delete=models.CASCADE)
    body = RichTextField()

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.user)


"""
I need to create a blog model so it would have 
* A header
* The post
* A comment session
* The author
* Date published 
* Related images
"""