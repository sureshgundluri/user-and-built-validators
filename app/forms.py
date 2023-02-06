from django import forms
from django.core import validators


def validate_for_s(value):
    if value[0]=='s':
        raise forms.ValidationError('somethig')
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length is too low')


class Nameform(forms.Form):
    name=forms.CharField(max_length=30,validators=[validate_for_s,validators.MaxLengthValidator(10)])
    age=forms.IntegerField()
    email=forms.EmailField()
    reemail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    modilenumber=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        p=self.cleaned_data['password']

        if e!=r:
            raise forms.ValidationError('not matched')
        if len(p)<=7:
            raise forms.ValidationError('password too low')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot catched')
