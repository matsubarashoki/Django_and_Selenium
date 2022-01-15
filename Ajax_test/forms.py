from django import forms
from django.db import models
from django.forms import fields
from .models import ActualWork

class ActualWorkForm(forms.ModelForm):
    class Meta:
        model = ActualWork
        fields = '__all__'

