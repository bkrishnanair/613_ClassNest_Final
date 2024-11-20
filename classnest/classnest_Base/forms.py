from django import forms
from .models import Course, Discussion, Inbox

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['course', 'title', 'content']

class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox
        fields = ['to', 'subject', 'message']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']

# Add this class to handle user registration
class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="I am a")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']
