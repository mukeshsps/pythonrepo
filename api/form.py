from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    user = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())
   
class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
    
class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('username', 'password')
        def clean(self):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            if username.blank:
                raise forms.ValidationError("username is required")
            if password.blank:
                raise forms.ValidationError("password is required")
            return self.cleaned_data       
