from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

def index(request):

    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10]

    #print(contacts.query)

    context = {
        'contacts' : contacts,
        'site_title' : "Contatos"
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):

    #singles_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact =  get_object_or_404(Contact, 
                        pk=contact_id, show=True)
    #if singles_contact is None:
    #    raise Http404()
    #print(contacts.query)
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
