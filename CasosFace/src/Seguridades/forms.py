#from django.forms import  ModelForm
from google.appengine.ext.db import djangoforms
#import google.appengine.ext.db.djangoforms as forms
#from django import forms
from Seguridades.models import Author,  Book
#from django.newforms import form_for_model

#AuthorForm = form_for_model(Author)

class AuthorForm(djangoforms.ModelForm):
    class Meta:
        model = Book