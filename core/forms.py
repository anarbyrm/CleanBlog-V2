from django import forms
from .models import Post, Contact


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content']



class ContactForm(forms.ModelForm):
   class Meta:
       model = Contact
       fields = ['name', 'email', 'message']