from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('name', 'telephone','question')