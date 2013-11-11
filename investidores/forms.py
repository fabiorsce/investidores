from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from investidores.models import Desejo
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
import hashlib

from django import forms
from django.forms.util import flatatt
from django.template import loader
from django.utils.datastructures import SortedDict
from django.utils.html import format_html, format_html_join
from django.utils.http import int_to_base36
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD, identify_hasher
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site



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
    
    
class AutenticaUsuarioForm(AuthenticationForm):
    
    username = forms.EmailField(help_text=_("Enter your email."))
    
    password = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    
    def clean(self):
        
        #email = self.cleaned_data.get('username')
        #username = User.objects.get(email=email).username
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'username': self.username_field.verbose_name
                    })
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data