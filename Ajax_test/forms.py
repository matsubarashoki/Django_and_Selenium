from calendar import c
import imp
from django import forms
from django.db import models
from django.forms import fields
from .models import ActualWork, TodoItem
from bootstrap_modal_forms.forms import BSModalForm


class ActualWorkForm(BSModalForm):
    class Meta:
        model = ActualWork
        fields = ['matter_id','emp_name','actual_time_unit','actual_time',
        'over_time','payment','deducting','excess','over_amount',
        'special_item1','special_item1_amount','special_item2',
        'special_item2_amount','total_amount','billing_date',
        'deadline','work_duration','contract_duration']

class CreateUpdateTodoItemForm(BSModalForm):
    class Meta:
        model = TodoItem
        fields = ['item']