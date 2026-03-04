from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
                'id': 'floatingUsername'
                })
            
        self.fields['password1'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Пароль',
                'id': 'floatingPassword1'
                })
            
        self.fields['password2'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Подтвердите Пароль',
                'id': 'floatingPassword2'
                })