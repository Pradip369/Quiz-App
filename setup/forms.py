from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={'required':"Enter name"},widget=forms.TextInput(attrs={'rows':1,'placeholder':'Enter Full Name'}),min_length=3)
    mobile_no = forms.CharField(error_messages={'required':"Enter mobile no."},widget=forms.TextInput(attrs={'rows':1,'placeholder':'Enter Mobile No.'}),max_length=10,min_length=8)
    email = forms.EmailField(error_messages={'required':"Enter email"},widget=forms.TextInput(attrs={'rows':1,'placeholder':'Enter Email Address'}))
    city = forms.CharField(error_messages={'required':"Enter city"},min_length=2,widget=forms.TextInput(attrs={'rows':1,'placeholder':'Enter City'}))
    address = forms.CharField(min_length=12,error_messages={'required':"Enter address"},widget=forms.Textarea(attrs={'rows':2,'cols':4,'placeholder':"Enter Full Address(e.g. House no.,soc. or aprt. name,area,zipcode,etc)"}))
