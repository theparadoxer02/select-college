from django import forms
from .models import City, Courses


class UserInputForm(forms.Form):
    level_choices = (
        ('graduation', 'graduation'),
        ('post-graduation', 'post-graduation')
    )
    city = forms.ModelChoiceField(queryset=City.objects.all())
    course = forms.ModelChoiceField(queryset=Courses.objects.all())
    level = forms.ChoiceField(choices=level_choices)
