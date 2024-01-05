from django.shortcuts import render
from portfolio.models import Project, WorkExperience
from mailjet_rest import Client
MJ_APIKEY_PUBLIC= 'e56e454a0e879bf7f7c3750bc7935aa1'
MJ_APIKEY_PRIVATE= '5cd1fee59accf9886c38a077f396b523'
# Create your views here.
def index(request):
    projects = Project.objects.all()
    
    # Split responsibilities and convert them to a list
    for project in projects:
        project.responsibilities = project.responsibilities.split(',')
    
    experiences = WorkExperience.objects.all()

    for experience in experiences:
        experience.description = experience.description.split(',')

    return render(request, 'index.html', {'projects': projects, 'experiences': experiences})

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comments = request.POST.get('comments')

        # Your Gmail address to receive the email
        to_email = 'vipin11dadhich+portfolio@gmail.com'
        api_key =MJ_APIKEY_PUBLIC
        api_secret =MJ_APIKEY_PRIVATE
        mailjet = Client(auth=(api_key, api_secret))
        # Construct the email message
        message = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact</title>
        </head>
        <body>
            Name: {name}\nEmail: {email}\nSubject: {subject}\nComments: {comments}
        </body>
        </html>
        """
        data = {
            'FromEmail': 'md.codertie@gmail.com',
            'FromName': f'Vipin Portfolio | contact by {name} - {email}',
            'Subject': 'Contact from prtfolio',
            'Html-part': message,
            'Recipients': [{'Email':to_email}]
        }

        result = mailjet.send.create(data=data)
        print(result.status_code)
    
    projects = Project.objects.all()
    
    # Split responsibilities and convert them to a list
    for project in projects:
        project.responsibilities = project.responsibilities.split(',')
    
    experiences = WorkExperience.objects.all()

    for experience in experiences:
        experience.description = experience.description.split(',')

    return render(request, 'index.html', {'projects': projects, 'experiences': experiences})