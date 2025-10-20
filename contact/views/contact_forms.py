from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = ('firts_name',
                  'last_name',
                  'phone',
                  'email',
                  )
    def clean(self):
        cleaned_data =  self.cleaned_data
        
        self.add_error(
            None, ValidationError(
                'Mensagem de Error',
                code='invalid'
            )
            
        )

        return super().clean()

def create(request :HttpRequest):
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST)
            }

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
            'form': ContactForm()
            }

    return render(
            request,
            'contact/create.html',
            context
        )

   

