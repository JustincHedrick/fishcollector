from django.forms import ModelForm
from .models import caughtFish

class caughtForm(ModelForm):
  class Meta:
    model = caughtFish
    fields = ['date', 'fish']