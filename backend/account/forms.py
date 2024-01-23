from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'password1', 'password2')
