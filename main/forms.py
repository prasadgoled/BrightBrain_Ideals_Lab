from django import forms
from.models import ideaDetails
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from captcha.fields import CaptchaField

class ideaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ideaForm, self).__init__(*args, **kwargs)
        placeholders = {
            'businessName': 'Idea Name',
            'businessLocation': 'Location where you want to start',
            'businessType': 'Your Business Type',
            'investmentAmount': 'Estimated Investment',
            'contractDuration': 'Agreement Period',
            'numberOfPeople': 'Investors Count',
            'businessDescription': 'Describe your business concept'
        }
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders.get(field, '')

            # Adding form-control class
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = ideaDetails
        fields = ['businessName', 'businessLocation', 'businessType', 'investmentAmount', 'contractDuration', 'numberOfPeople', 'businessDescription']
        widgets = {'businessDescription': forms.Textarea()}

class CustomCaptchaField(CaptchaField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.attrs['class'] = 'form-control'
        self.widget.attrs['placeholder'] = 'Enter Captcha'

class signupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}))
    captcha = CustomCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        }
        
class loginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = False
        self.fields['username'].widget = forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': _('Username'),
            'class': 'form-control',
            'aria-describedby': 'username-addon',
        })
        
        self.fields['password'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'placeholder': _('Password'),
            'class': 'form-control',
            'aria-describedby': 'password-addon',
        })
