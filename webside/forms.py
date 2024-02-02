from django import forms

class CallbackForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class':"form-control"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-Mail Address', 'class':"form-control"}))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class':"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class':"form-control"}))
    phone_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':"form-control"}))
