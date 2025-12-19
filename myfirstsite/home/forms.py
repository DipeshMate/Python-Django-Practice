from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=70)