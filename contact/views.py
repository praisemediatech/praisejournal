# from django.shortcuts import render
# from .import forms
# from django.conf import settings
# from .forms import ContactForm
# from django.shortcuts import reverse

# def mail(request):
#     template = 'mail.html'
#     context = {}
#     contactform = ContactForm(request.POST or None)
#     if contactform.is_valid():
#         name = forms.cleaned_data['name']
#         subject = 'message from website.com'
#         content = forms.cleaned_data['message']
#         message = f'{name}/n{content}'
#         emailTo = [settings.EMAIL_HOST_USER]
#         send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
#     context['contactform'] = contactform 
#     return render(request, template, context)