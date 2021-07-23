from django import forms
from django.forms import ModelForm, Textarea

from ckeditor.fields import RichTextField

from .models import *

class DatePicker(forms.DateInput):
	input_type = 'date'
		

class EditProfileForm(ModelForm):
	first_name = forms.CharField(
        widget=forms.TextInput(attrs={
        	'placeholder': 'First name' , 
        	'class': 'form-control',
        	})
        )
	middle_name = forms.CharField(
		required=False,
        widget=forms.TextInput(attrs={
        	'placeholder': 'Middle name' , 
        	'class': 'form-control',
        	})
        )
	last_name = forms.CharField(
        widget=forms.TextInput(attrs={
        	'placeholder': 'Last name', 
        	'class': 'form-control',
        	})
        )
	email = forms.EmailField(
        widget=forms.EmailInput(attrs={
        	'placeholder': 'Email', 
        	'class': 'form-control',
        	})
        )
	birthdate = forms.CharField(
        widget=DatePicker(attrs={
        	'class': 'form-control',
        	})
        )
	bio = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 3, 
			'placeholder': 'Write a little about your self!'
			})
		)

	GENDER_CHOICES = (
    		('M', 'Male'),
    		('F', 'Female'),
    	)
	gender = forms.ChoiceField(
		label="",
		choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
        )

	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['user']


class BlogPostForm(forms.ModelForm):
	title = forms.CharField(
		label="",
        widget=forms.TextInput(attrs={'placeholder': 'Blog Title'})
        )
	content = RichTextField()

	class Meta:
		model = BlogPost
		fields = '__all__'
		exclude = ['author', 'categories', 'likes']


class CommentForm(forms.ModelForm):
	body = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 3, 
			'placeholder': 'Join the discussion and leave a comment!'
			})
		)
	class Meta:
		model = Comment
		fields = ['body']

	
		