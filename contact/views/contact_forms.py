from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

def create(request :HttpRequest):
    form_action =  reverse('contact:create')


    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        context = {
            'form': form,
            'form_action' :  form_action
            }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id = contact.id )

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
            'form': ContactForm(),
            'form_action' :  form_action
            }


    return render(
            request,
            'contact/create.html',
            context
        )

   
def update(request :HttpRequest, contact_id):
    form_action =  reverse('contact:update', args=(contact_id,))
    contact = get_object_or_404(Contact, id=contact_id,show = True)

    if request.method == 'POST':
        form = ContactForm(data=request.POST,instance=contact) # ja tenho a instancia acriada

        context = {
            'form': form,
            'form_action' :  form_action
            }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id = contact.id )

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
            'form': ContactForm(instance=contact),
            'form_action' :  form_action
            }


    return render(
            request,
            'contact/create.html',
            context
        )

   

