from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):


    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'image/*'
            }
        )
    )

    class Meta:
        model =  Contact
        fields = ('firts_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category',
                  'picture',
                  )
        #Existe forma de fazer pelo init ou recriando  campo novamente
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'placeholder': 'Digite o número'}),
        #     'last_name': forms.PasswordInput(render_value=True),
        #     'firts_name': forms.PasswordInput(attrs={'placeholder': 'Escreva Aqui'})
        # }

    # def clean(self):
    #     cleaned_data =  self.cleaned_data
        
    #     self.add_error(
    #         None, ValidationError(
    #             'Mensagem de Error',
    #             code='invalid'
    #         )
            
    #     )

    #     return super().clean()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            'email' ,
            "username",
             'password1',
             'password2'   ,       

        )
    def clean_email(self):
        email =  self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError("Ja existe este email",code='invalid')
            )

        return email