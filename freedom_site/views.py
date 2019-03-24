from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Account

# Create your views here.
def home(req):
    return render(req, 'home.html')

def contact(req):
    return render(req, 'contact.html')

def apply(req):
    if req.method == 'GET':
        return render(req, 'apply.html', {'msg':''})
    if req.POST:
        user = req.POST['name']
        semester = req.POST['sem']
        phone = req.POST['phone']
        email = req.POST['email']
        usn = req.POST['usn']
        if len(Account.objects.filter(phone=phone)) or len(Account.objects.filter(email=email)) or len(Account.objects.filter(usn=usn)):
            return render(req, 'apply.html', {'msg': "Someone (possibly you) has already applied with that email, phone number, or USN."})

        other = req.POST.get('other', '')
        other_data = req.POST.get('other-value', '')
        if other and not other_data:
            return render(req, 'apply.html', {'msg': "You need to specify which other field you're interested in"})
        web = req.POST.get('Web', '')
        ml = req.POST.get('ML', '')
        app = req.POST.get('App', '')
        networking = req.POST.get('Networking', '')
        if not web and not ml and not app and not networking:
            return render(req, 'apply.html', 'You need to choose at least one field of interest')
        web = web if not web else web + '\n'
        ml = ml if not ml else ml + '\n'
        app = app if not app else app + '\n'
        networking = networking if not networking else networking + '\n'

        interests = web + ml + app + networking + other_data

        statement = req.POST['statement']
        skills = req.POST['skills']
        account = Account(semester=sem, name=user, email=email, phone=phone, usn=usn, personal_statement=statement, skills=skills, interests=interests)
        account.save()


        return render(req, 'apply.html', { 'msg':'You have successfully applied! We\'ll email you in a bit'})

def webpage(req):
    return render(req, 'webpage.html')
