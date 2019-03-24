from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Account

# Create your views here.
def home(req):
    return render(req, 'home.html')

def contact(req):
    return render(req, 'contact.html')

def login(req):
    return render(req, 'login.html')

def register(req):
    if req.method == 'GET':
        return render(req, 'login.html', {'msg':''})
    if req.POST:
        other = req.POST.get('other', '')
        other_data = req.POST.get('other-value', '')
        if other and not other_data:
            return render(req, 'login.html', {'msg': "You need to specify which other field you're interested in"})
        web = req.POST.get('Web', '')
        ml = req.POST.get('ML', '')
        app = req.POST.get('App', '')
        networking = req.POST.get('Networking', '')
        if not web and not ml and not app and not networking:
            return render(req, 'login.html', 'You need to choose at least one field of interest')
        web = web if not web else web + '\n'
        ml = ml if not ml else ml + '\n'
        app = app if not app else app + '\n'
        networking = networking if not networking else networking + '\n'

        interests = web + ml + app + networking + other_data
        user = req.POST['name']
        phone = req.POST['phone']
        email = req.POST['email']
        usn = req.POST['usn']

        statement = req.POST['statement']
        skills = req.POST['skills']
        account = Account(email=email, phone=phone, usn=usn, personal_statement=statement, skills=skills, interests=interests)
        try:
            account.save()
        except:
            return render(req, 'login.html', {'msg':'Someone has already applied with that USN or Email'})

        return render(req, 'login.html', { 'msg':'<span style="color: white">You have successfully applied! We\'ll email you in a bit</span>'})

def webpage(req):
    return render(req, 'webpage.html')
