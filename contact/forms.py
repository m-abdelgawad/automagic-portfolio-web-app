# sendemail/forms.py
from django import forms
# Import the phone number field
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):

    # Full name
    name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name...',
            },
        ),
        error_messages={'required': 'Please let me know what to call you!'},
    )

    # Email address
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            }
        )
    )

    # Phone number
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            initial='EG',
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'placeholder': '(123) 456-7890',
            }
        )
    )

    # Email message
    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message here...',
                'style': 'height: 10rem;',
            }
        )
    )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
