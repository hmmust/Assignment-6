import datetime

import django.core.exceptions
from django import forms
from .models import Owner,Car

def check_age(value):
    if int(value) < 0:
        raise django.core.exceptions.ValidationError("Age must be above 0")

class CarModelForm(forms.ModelForm):
    class Meta:
        model= Owner
        fields = "__all__"
class CarForm(forms.Form):

    id = forms.IntegerField(max_value=500)
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Car Type name'}))
    type= forms.ChoiceField(choices=[(1, "Truck"),(2, "Sedan")],widget=forms.Select, initial=2)
    active= forms.BooleanField(widget=forms.CheckboxInput, required=False)
    address= forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(validators=[check_age],initial=18)
    issuedate = forms.DateField(initial= datetime.date(2023,12,1), widget=forms.NumberInput(attrs={'type':'date'}))
    email = forms.RegexField(widget=forms.TextInput(attrs={"placeholder":"ahmad@uop.edu.jo"}),regex="[0-9A-Za-z\.\_]+@uop(std)?.edu.jo", error_messages={"invalid":"Enter a valid UoP Email"})
    url= forms.RegexField(regex='[0-9]{5}',error_messages= {'invalid':"Enter five digits number"},required=False,widget=forms.NumberInput)