from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Content, Document
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('header', 'body')

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('header', 'description', "content_type", 'topic', 'link_to_source', 'content_creator')
        labels = {
            "header": "Überschrift",
            "description": "Beschreibung",
            "content_type": "Art des Inhalts",
            'topic': "Thema",
            'link_to_source': "Quelle (URL)",
            'content_creator': "Autor/in"
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    gender = forms.ChoiceField(choices=(("1", "Male"),
                                        ("2", "Female"),
                                        ("3", "Diverse"),
                                        ("4", "Prefer not to say")))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

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

    # def clean(self):
    #     ca = self.request.POST["g-recaptcha-response"]
    #     url = "https://www.google.com/recaptcha/api/siteverify"
    #     params = {
    #         'secret': config.RECAPTCHA_SECRET_KEY,
    #         'response': ca,
    #         'remoteip': utility.get_client_ip(self.request)
    #     }
    #     verify_rs = requests.get(url, params=params, verify=True)
    #     verify_rs = verify_rs.json()
    #     status = verify_rs.get("success", False)
    #     if not status:
    #         raise forms.ValidationError(
    #             _('Captcha Validation Failed.'),
    #             code='invalid',
    #         )

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["name", "topic", "description" ,"docfile"]



    