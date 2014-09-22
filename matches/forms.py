from django import forms
from models import CrowdResult

class CrowdResultForm(forms.Form):
  home_goals = forms.DecimalField(max_digits=5, decimal_places=0)
  away_goals = forms.DecimalField(max_digits=5, decimal_places=0)

