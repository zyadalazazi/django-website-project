from django.forms import forms


class UserAuth(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.Charfield()
