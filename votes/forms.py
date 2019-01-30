from django.forms import ModelForm
from .models import Candidate, Position, Vote

class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id', 'position']

class PositionModelForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']
