from django import forms
    

class Registration(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'enter your email'}))
    birth = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'date of birth'}))
    

class Newform(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'enter your email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'phone'}))
