from django import forms
from.models import ideaDetails
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class ideaForm(forms.ModelForm):
    class Meta:
        model=ideaDetails
        fields=['businessName','businessLocation','businessType','investmentAmount','contractDuration','numberOfPeople','businessDescription']
        labels={
            'businessName':'Idea Name',
            'businessLocation':'Loaction where you want to do',
            'businessType':'Your Business Type',
            'investmentAmout':'Estimated Investment',
            'contractDuration':'Agreement Period',
            'numberOfPeople':'Investors Count',
            'businessDescription':'Describe your business concept'
            }
        widgets={'businessDescription':forms.Textarea()}

class signupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'ftext'}))
    password2=forms.CharField(label='Re-enter Password',widget=forms.PasswordInput(attrs={'class':'ftext'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'ftext'}),
                 'first_name':forms.TextInput(attrs={'class':'ftext'}),
                 'last_name':forms.TextInput(attrs={'class':'ftext'}),
                 'email':forms.EmailInput(attrs={'class':'ftext'}),
                 }
        
class loginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'ftext'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'ftext'}))