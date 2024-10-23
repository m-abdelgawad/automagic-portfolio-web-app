from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):

    sent = False

    if request.method == 'POST':
        # Form was submitted

        form = ContactForm(request.POST)

        if form.is_valid():
            # Form fields passed validation

            cd = form.cleaned_data

            subject = '{0} Just Sent You a Message'.format(
                cd['name']
            )

            body = 'Hi,\n\n' + \
                '"{0}" just sent you the following message.\n' + '-'*20 + \
                '\n{1}\n' + '-'*20 + '\n' + \
                'Phone Number: {2}\n' + 'Email Address: {3}\n\n' + \
                'Thanks and best regards,\n' +  \
                'Mohamed from AutoMagic Developer'

            body = body.format(cd['name'], cd['message'], cd['phone'], cd['email'])

            send_mail(subject, body, settings.EMAIL_HOST_USER,
                      ['muhammadabdelgawwad@gmail.com'])

            sent = True

    # If the request is not POST
    else:

        form = ContactForm()

    return render(request, 'contact/contact.html',
                  {'form': form, 'sent': sent, })