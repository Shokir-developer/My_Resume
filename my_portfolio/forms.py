from django import forms
from .models import SendModel


class SendForm(forms.ModelForm):
    class Meta:
        model = SendModel
        fields = '__all__'

        widgets = {
            'fish': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'F.I.SH'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter an email'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
