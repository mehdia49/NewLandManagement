from django import forms

class usersForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    lastname = forms.CharField(label='Last Name', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    DOB = forms.DateField(label='Birth Date', widget=forms.DateInput(attrs={'placeholder': 'Enter DOB'}))
    city = forms.ChoiceField(label='Select your city name', choices=[('lahore', 'Lahore'), ('sahiwal', 'Sahiwal'), ('okara', 'Okara')], widget=forms.Select())
    phone = forms.CharField(label='Phone Number', max_length=11, widget=forms.TextInput(attrs={'placeholder': '03xx xxxxxxx'}))
    email = forms.EmailField(label='Your Email ID', widget=forms.TextInput(attrs={'placeholder': 'email id'}))
