from django import forms

from account.models import Role,UserAccount,User

class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':"form-control border border-primary"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control border border-primary"
            }
        )
    )
class RoleForm(forms.ModelForm):
     class Meta:
        model=Role
        fields='__all__'

class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
# class DefaultUserForm(forms.Form):
#     class Meta:
#         model=UserAccount
#         fields='__all__'
class AddAccountForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=['Role','username']