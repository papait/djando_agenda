from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.http import HttpRequest
from django.core.paginator import Paginator


def index(request :HttpRequest):

    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj =  paginator.get_page(page_number)

    print(page_obj)

    context = {
        'page_obj' : page_obj,
        'site_title' : "Contatos"
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request :HttpRequest, contact_id):

    #singles_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact =  get_object_or_404(Contact, 
                        pk=contact_id, show=True)
    #if singles_contact is None:
    #    raise Http404()
    #print(single_contact.query)
    contact_name = f'{single_contact.firts_name} {single_contact.last_name} - '


    context = {
        'contact' : single_contact,
        'site_title' : contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request :HttpRequest):
    search_value = request.GET.get('q','').strip() #Name do form no header

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(Q(firts_name__icontains=search_value)  |
                Q(last_name__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj =  paginator.get_page(page_number)

    #print(contacts.query) Pra ver a consulta

    context = {
        'page_obj' : page_obj,
        'site_title' : "Contatos",
        'search_value' : search_value
    }

    return render(
        request,
        'contact/index.html',
        context
    )
