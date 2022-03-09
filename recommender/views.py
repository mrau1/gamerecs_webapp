from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from .forms import EntryForm
from .models import Entry
from .forms import InputForm

'''from .models import xyz'''
# request handler!

# create view ==> add to urls.py here, then in parent class.


# def rec_home(request):
#     return render(request, 'rec_home.html')  # , context=context)            

@login_required
def add_entry(request, *args, **kwargs):
    form = EntryForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = EntryForm()  # returned cleaned form
        # return HttpResponseRedirect("/success") # two options for redirecting after form submission
        # return redirect("/success")
    return render(request, "forms.html", {"form": form})

def newInput(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        return redirect("/")
    else:
        form = InputForm()
    return render(request, "newInput.html", {"form": form})   
