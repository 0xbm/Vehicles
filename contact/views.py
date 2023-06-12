from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from datetime import datetime


def index(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail("The contact from subject", "This is the message", 'noreply@gmail.com', ['automobile@gmail.com'],
                      html_message=html)
            return redirect("automobiles:index")
    else:
        form = ContactForm()

    context = {"form": form, "current_year": current_year, 'time': time}
    return render(request, "contact/index.html", context)
