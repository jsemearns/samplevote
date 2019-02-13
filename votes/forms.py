from django.forms import ModelForm
from .models import Candidate, Position, Vote
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput


class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id', 'position']

class PositionModelForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']

class RegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
        }
