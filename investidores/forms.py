from django.contrib.auth.forms import UserCreationForm
from django import forms
from investidores.models import Desejo
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
import hashlib


class DesejoForm(forms.ModelForm):
    class Meta:
        model = Desejo
        
        
class CriaUsuarioForm(forms.Form):
    
    error_messages = {'duplicate_email': "O email informado ja esta sendo utilizado por outro usuario",
                      'password_mismatch': "As senhas informadas nao conferem",
                     }
    
    nome = forms.CharField(help_text=_("Enter your name."))
    
    email = forms.EmailField(help_text=_("Enter your email."))
    
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))
    
    
    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        username = hashlib.sha1(email.encode('utf-8')).hexdigest()[0:29]
        
        try:
            User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            return email
            #return hashlib.sha1(email.encode('utf-8')).hexdigest()[0:29]
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    
    def save(self, commit=True):
        user = User()
        user.username = hashlib.sha1(self.cleaned_data["email"].encode('utf-8')).hexdigest()[0:29]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["nome"]
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user
    
    
