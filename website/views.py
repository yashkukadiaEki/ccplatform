from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings

def gcp(request):
    return render(request, 'website/gcp.html')

def azure(request):
    return render(request, 'website/azure.html')

def aws(request):
    return render(request, 'website/aws.html')

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')
        
def service(request):
    return render(request, 'website/service.html')

def data_collection(request):
    return render(request, 'website/data_collection.html')
def segmentation(request):
    return render(request, 'website/segmentation.html')
def consolidation(request):
    return render(request, 'website/consolidation.html')
def activation(request):
    return render(request, 'website/activation.html')
def ds_usecase(request):
    return render(request, 'website/ds_usecase.html')
def dashboarding(request):
    return render(request, 'website/dashboarding.html')





def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request):
    return render(request, 'website/blog_details.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        
        #send email to default address
        send_mail(
            'Follow up required for - ' + name,
            message,
            email,
            [conf_settings.CONTACT_US_FORM_EMAIL_TO],
            fail_silently=False,
        )

        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'website/contact.html')


