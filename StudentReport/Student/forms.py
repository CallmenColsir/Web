from django import forms
from .models import StudentData

class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = StudentData
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name: '}),
            'major': forms.TextInput(attrs={'placeholder': 'Enter Major: '})
        }
        fields = ['name', 'age', 'major']
        
