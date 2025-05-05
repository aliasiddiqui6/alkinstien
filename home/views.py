from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Contact
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

# @login_required
def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send email
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email='your_email@example.com',
            recipient_list=['sanamarch25@gmail.com'],
            fail_silently=False,
        )

        # Display success message
        messages.success(request, 'Your message has been sent successfully!')

        return redirect('index')

    return render(request, 'index.html')
