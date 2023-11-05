from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
import os
from django.conf import settings


class Homepage(View):
    template_name = "homepage.html"

    def post(self, request):
        hr_email = request.POST.get('email')
        if not hr_email.strip():
            messages.error(request,'Please enter a mail')
            return redirect('Homepage')
        mail_subject = 'Application for Python Django Developer Position'
        
        message = '''
        Hello,

        I'm Mohammed Sifan KP, a passionate Python Django and React developer. I've embarked on a self-learning journey, mastering Python, Django, and React, resulting in the completion of two significant projects and four smaller ones. Not only do I excel in software development, but I also possess proficiency in computer hardware and networking projects.

        One of my flagship projects is "Ebuds Ecommerce," which integrates RazerPay payment solutions with a user-friendly UI. I meticulously crafted the frontend using HTML and Django for the backend, ensuring a seamless experience. The system includes a two-layer administration system for optimal control and user satisfaction.

        Another remarkable project of mine is "JobPorter," aptly named as a career bridge. In this project, I implemented a wide array of backend features using Django, such as Radis, Celery, Signals, REST framework, and Channels for real-time communication. On the frontend, I utilized React with Vite and Redux to enable temporary data storage for users. The site comprises three layers: admin, company, and user, providing a comprehensive solution for all stakeholders.

        It's worth noting that I've hosted my website on AWS, ensuring reliability and scalability for seamless user access. If you're seeking a developer who combines expertise in Python, Django, React, and a strong foundation in hardware and networking, I'd be thrilled to contribute to your projects.

        Contact no : +919562040856
        git rep : https://github.com/MOHAMMESIFANKP
        Linkedin : https://www.linkedin.com/in/mohammed-sifan-b2546b18a/
        '''

        to_email = hr_email
        send_email = EmailMessage(mail_subject, message, to=[to_email])

        pdf_file_path = os.path.join(settings.BASE_DIR, 'templates', 'mohammedsifankpresume.pdf')
        send_email.attach_file(pdf_file_path) 

        try:
            send_email.send()
            messages.success(request, 'Mail sent successfully')
        except Exception as e:
            messages.error(request, f'Failed to send email: {str(e)}')

        return redirect('Homepage')  

    def get(self, request):
        return render(request, self.template_name)
