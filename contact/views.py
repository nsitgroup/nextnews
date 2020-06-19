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

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def contactForm(request):
    form = ContactForm
    target = TargetForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            contact_firstname = request.POST.get('firstname')
            contact_lastname = request.POST.get('lastname')
            contact_email = request.POST.get('email')
            contact_subject = request.POST.get('subject')
            contact_content = request.POST.get('message')
            contact = form.save(commit=False)
            contact.save()
            
            """
            send_mail(
                contact_subject,
                contact_content,
                contact_email,
                ['nsitsenegal@gmail.com'],
                fail_silently=False,
            )"""
            context = {
                'name': contact_firstname
            }
            
            subject = 'Subject'
            html_message = render_to_string('contact/mail_template.html', context)
            plain_message = strip_tags(html_message)
            from_email = '<from@example.com>'
            to = contact_email
            
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            return redirect('home')
        
    context = {
        "form": form,
        "target": target
    }
    return render(request, 'contact/contact_create.html', context)


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