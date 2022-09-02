from dataclasses import field
from operator import imod
from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
     class Meta:
        model = Room
        fields = "__all__"