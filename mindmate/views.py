from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def home(request):
    
    return render(request, 'index.html', {'current_page': 'home'})

def services(request):
      return render(request, 'services.html', {'current_page': 'services'})

def assessment(request):
    return render(request, 'assessment.html', {'current_page': 'assessment'})

def contact(request):
    return render(request, 'contactus.html', {'current_page': 'contact'})

def login(request):
    return render(request, 'services.html', {'current_page': 'services'})

def about(request):
    return render(request, 'aboutus.html')

def nav(request):
    return render(request, 'nav.html')

@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        send_mail(subject,body,'settings.EMAIL_HOST_USER',['college2020online@gmail.com'],fail_silently=False)
        #email = EmailMessage(subject, body=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}', from_email='django.mailtrap.club', to=['karthickthasan.s2020@kgkite.ac.in'])
        

        #send_mail(subject, f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}', from_email='django.mailtrap.club', recipient_list=['userunknown3010@gmail.com'])

        return render(request, 'contactus.html')

    

