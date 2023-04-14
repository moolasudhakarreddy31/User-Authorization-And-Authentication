from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    class Meta:
        model=User
        fields=['username','password','email','firstname','lastname']
        # fields = "__all__"
