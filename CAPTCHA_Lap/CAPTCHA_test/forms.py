from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    gender = forms.ChoiceField(choices=(("1", "Male"),
                                        ("2", "Female"),
                                        ("3", "Diverse"),
                                        ("4", "Prefer not to say")))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "gender", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user
