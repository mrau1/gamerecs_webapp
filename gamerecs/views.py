
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from recommender.forms import EntryForm
from recommender.models import Entry
from recommender.forms import InputForm
# create view ==> add to urls.py here, then in parent class.

def home(request):
    return render(request, 'home.html') #, context=context)

    #return HttpResponse('HOME PAGE \n Welcome to our capstone website')
def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        return redirect("/")
    else:
        form = InputForm()
    return render(request, "newInput.html", {"form": form})
