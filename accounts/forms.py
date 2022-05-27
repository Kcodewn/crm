from ast import Mod
from pyexpat import model
from re import L
from statistics import mode
from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'