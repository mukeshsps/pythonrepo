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

"""class UserChangeForm(BaseModelForm): 
    def clean_email(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
        return email.lower()   """     

"""class MyLoginForm(forms.ModelForm):
    username = forms.CharField(label="email")
    class Meta:
        model = User
        field = ('username', 'password')
        labels = {
            "username": "email"
            }"""
    
    
"""def clean_message(self):
       username = self.cleaned_data.get("username")
       dbuser = User.objects.filter(name = username)
       
       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       return username"""

"""class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100)
    picture = forms.ImageFields(upload_to = 'pictures')"""

"""class TrustForm(forms.ModelForm):
    class Meta():
        model = Trust

class TrustAdministration(forms.ModelForm):
    class Meta():
        model = TrustAdministration

class UserCreateForm(UserCreationForm):
    class Meta():
        model = User"""


"""class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email",)
        
class CustomUserChangeForm(UserChangeForm):
    
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = "__all__" """
        
"""class PasswordResetForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
 
    # removed some parameters that I didn't use
    def save(self, subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             token_generator=default_token_generator,
             from_email=None, html_email_template_name=None):
        Generates a one-use only token for resetting password and sends to the
        user.
        &amp;quot;&amp;quot;&amp;quot;
        from django.core.mail import send_mail
        # for some applications I use separate models for Django Admin/Web and API
        # get_api_user_model() returns my ApiUser, use django.contrib.auth.get_user_model()
        # for user model defined in settings.AUTH_USER_MODEL
        UserModel = get_api_user_model()
        email = self.cleaned_data[&amp;quot;email&amp;quot;]
        active_users = UserModel._default_manager.filter(
            email__iexact=email, active=True)
        for user in active_users:
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            # I use application name for both, in the email then I can point the user
            # to the application with an url like: application://passwordreset/secret_code
            # which on IOS and Android should open the app
            site_name = settings.APPLICATION_NAME
            protocol = settings.APPLICATION_NAME.lower()
            c = {
                'email': user.email,
                'location': 'passwordreset',
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': protocol,
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
 
            if html_email_template_name:
                html_email = loader.render_to_string(html_email_template_name, c)
            else:
                html_email = None
            send_mail(subject, email, from_email, [user.email], html_message=html_email)
"""

