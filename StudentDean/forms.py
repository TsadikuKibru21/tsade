from dataclasses import field
from django import forms
from .models import *

class AddBlockForm(forms.ModelForm):
    class Meta:
        model=Block
        fields='__all__'
# class AddDorm(forms.ModelForm):
#     CHOICES = [('1','Active'),('0','Inactive')]
#     Status=forms.CharField(label='Status', widget=forms.RadioSelect(choices=CHOICES))
#     class Meta:
#         model=Dorm
#         fields='__all__'
class AddDorm(forms.ModelForm):
    CHOICES = [
        ('1', 'Active'),
        ('2', 'InActive'),
    ]

    # Block = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # Dorm_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # Capacity = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # ) 
    Status = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    class Meta:
        model = Dorm
        fields = '__all__'
    
class AddPlacementForm(forms.ModelForm):
    class Meta:
        model=Placement
        fields='__all__'