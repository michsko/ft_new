from django import forms
from django.forms import ModelForm
from .models import Event, User




class EventForm(forms.ModelForm):
	class Meta: 
		model = Event
		fields = ['name', 'date', 'venue', 'tickets', 'description',]
		labels = {'name':'', 'date':'YYYY-MM-DD HH:MM:SS', 'venue':'', 'tickets':'', 'description':'',}
		widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Představení'}),
		'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Datum'}),
		'venue': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Místo konání'}),
		'tickets': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vstupenky dostupne na:'}),
		'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Popis'})}