from django.forms import ModelForm
from .models import *

class login_form(ModelForm):
    class Meta:
        model=login
        fields='__all__' #to add specific fields fields=['name','password']