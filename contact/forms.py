from django.core.exceptions import ValidationError
from django.shortcuts import render
from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    firts_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='First Name',
        help_text='Texto de ajuda para seu usuário',
        )

    class Meta:
        model =  Contact
        fields = ('firts_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category'
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