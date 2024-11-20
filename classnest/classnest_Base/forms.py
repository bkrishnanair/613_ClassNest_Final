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