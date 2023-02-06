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
class GrantRoleForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=('User','Role')
class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'