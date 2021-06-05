from django import forms

class CreateFormForHeart(forms.From):
    name=forms.CharField(max_length=100)
    
