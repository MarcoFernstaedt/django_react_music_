from django.contrib.auth.form import UserCretionForm
from django.contib.auth.model import User

class SignUpForm(UserCretionForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']