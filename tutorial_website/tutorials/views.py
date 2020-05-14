from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import ProgrammingLanguage


# Create your views here.
def index(request):

    subjects = ProgrammingLanguage.objects.all()

    return render(request, 'index.html', {'subjects' : subjects})

#def learn_now(request, subject_id):
    subject = subject_id    
    return render(request, 'learn_now.html',  {'subject' : subject})


def learn_now(request, subject_id):
     subject = ProgrammingLanguage.objects.get(id=subject_id)
     return render(request, "learn_now.html", {"subject": subject})