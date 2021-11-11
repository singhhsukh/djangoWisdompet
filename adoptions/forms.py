from django import forms

class HashForm(forms.Form):

    text = forms.CharField(label="Enter your text here:",widget=forms.Textarea)