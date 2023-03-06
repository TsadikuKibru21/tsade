from dataclasses import field
from django import forms
from .models import *
from account.models import User
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['Id_no','FirstName','LastName','Gender','phone_no']
        widgets = {
        
            'Gender': forms.Select(attrs={'class': 'form-control'}),
        }
class AddBlockForm(forms.ModelForm):
    class Meta:
        model=Block
        fields='__all__'
        widgets = {
            'Block_name': forms.TextInput(attrs={'class': 'form-control' ,'readonly':'True'}),
            'Block_type': forms.Select(attrs={'class': 'form-control'}),
            'Block_purpose': forms.Select(attrs={'class': 'form-control'}),
            'Block_Capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }
class AddBlockForm1(forms.ModelForm):
    class Meta:
        model=Block
        fields='__all__'
        widgets = {
            'Block_name': forms.TextInput(attrs={'class': 'form-control' }),
            'Block_type': forms.Select(attrs={'class': 'form-control'}),
            'Block_purpose': forms.Select(attrs={'class': 'form-control'}),
            'Block_Capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }

# class AddDorm(forms.ModelForm):
#     CHOICES = [('1','Active'),('0','Inactive')]
#     Status=forms.CharField(label='Status', widget=forms.RadioSelect(choices=CHOICES))
#     class Meta:
#         model=Dorm
#         fields='__all__'
class AddDorm(forms.ModelForm):
    class Meta:
        model = Dorm
        fields = '__all__'
        widgets = {
            'Block': forms.Select(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }

    
class AddPlacementForm(forms.ModelForm):
    class Meta:
        model=Placement
        fields='__all__'