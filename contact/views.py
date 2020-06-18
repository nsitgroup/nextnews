from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404
from django.contrib import messages





# Contact form view

def contact(request):
    classe_active=5
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(request.POST)

        if form.is_valid():
            contact_name = request.POST.get('nom')
            contact_email = request.POST.get('Email')
            contact_subject = request.POST.get('Sujet')
            contact_content = request.POST.get('Message')
            contact = form.save(commit=False)
            contact.save()
            # TO DO Fix mail send

            send_mail(
                contact_subject,
                contact_content,
                contact_email,
                ['nsitsenegal@gmail.com'],
                fail_silently=False,
            )

            

            # msg = EmailMessage(contact_subject,
            #                    'Here is the message.', to=[contact_email])
            # msg.send()


            return redirect('home')

            #return redirect('blog:success')
    return redirect('home')


def contact_detail(request, contact_id):
    classe_active = 12
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404("La contact n'existe pas")
    return render(request, 'contact/contact_detail.html', locals())

def contact_list(request):
    classe_active = 12
    contacts = Contact.objects.all()

    return render(request, "contact/contact_list.html", locals())

def contact_delete(request, contact_id):

    contact= Contact.objects.filter(pk=contact_id)
    contact.delete()
    messages.success(request, "La contact a été supprimée avec succès !")
    contacts = Contact.objects.all()

    return redirect('contact:indexContact')