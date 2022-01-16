from calendar import c
import imp
from django import forms
from django.db import models
from django.forms import fields
from .models import ActualWork, TodoItem
from bootstrap_modal_forms.forms import BSModalForm


class ActualWorkForm(forms.ModelForm):
    class Meta:
        model = ActualWork
        fields = '__all__'

class CreateUpdateTodoItemForm(BSModalForm):
    class Meta:
        model = TodoItem
        fields = ['item']