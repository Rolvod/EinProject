from django.forms import ModelForm, TextInput, Textarea
from users.models import User

class ChangeProfile(ModelForm):
    class Meta:
        model = User
        fields = ['description', 'profile_picture', 'nickname']
        widgets = {'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),'profile_picture': TextInput(attrs={'class': 'form-control', 'placeholder': 'Аватарка'}),'nickname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Никнейм'})}