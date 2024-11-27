# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class RestaurantSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ['complaint_topic', 'complaint_Description', 'image1', 'image2', 'image3']
        widgets = {
            'complaint_topic': forms.Select(choices=[
                ('Unhygienic Environment', 'Unhygienic Environment'),
                ('Bad Quality Food', 'Bad Quality Food'),
                ('Bad Service', 'Bad Service'),
                ('Exceptionally High Price than MRP', 'Exceptionally High Price than MRP'),
                ('Foreign Object in Food', 'Foreign Object in Food'),
                ('Wait Time too Long', 'Wait Time too Long'),
            ]),}
        
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ['name', 'location', 'cuisine', 'image']  # Adjust fields as per your model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'cuisine': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PendingRestaurantForm(forms.ModelForm):
     class Meta:
        model = PendingRestaurant
        fields = ['name', 'location', 'address', 'cuisine']
        


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    phone_number = forms.CharField(max_length=15, label='Phone Number', required=False, widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number'}))
    message = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'placeholder': 'Your Message Here', 'rows': 5}))
    subject = forms.ChoiceField(choices=[('Feedback', 'Feedback'), ('Inquiry', 'Inquiry'), ('Complaint', 'Complaint')], label='Subject')

class ProfileForm(forms.ModelForm):

    # email = forms.EmailField(
    #     label="Email Address",
    #     widget=forms.EmailInput(attrs={'class':'form-control'}),
    # )
    class Meta:
        model = Profile
        fields = ['name','bio', 'address', 'profile_picture', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget = forms.FileInput(attrs={'class': 'form-control'})  # Removes clear checkbox


    