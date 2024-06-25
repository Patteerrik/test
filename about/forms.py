from django import forms

class CollaborateForm(forms.Form):
    
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

