from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()



