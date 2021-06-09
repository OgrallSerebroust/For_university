from django import forms
from .models import Theatre, Show, Visitor


class TheatreForm(forms.ModelForm):
    class Meta:
        model = Theatre
        fields = '__all__'


class ShowsForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
