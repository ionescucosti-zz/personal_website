from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Messages


class CreateNewPageForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text',
                                                                     'rows': 10}))


def home(request):
    return render(request, "index.html", {})


def resume(request):
    return render(request, "resume.html", {})


def projects(request):
    return render(request, "projects.html", {})


def single_page(request):
    return render(request, "indexsass.html", {})


def indexmpower(request):
    return render(request, "indexmpower.html", {})


def contact(request):
    if request.method == "POST":
        form = CreateNewPageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            msg = Messages(name=name, email=email, subject=subject, message=message)
            msg.save()
            return render(request, "contact.html", {
                'form': CreateNewPageForm(),
                "save": True
            })
        else:
            return render(request, "contact.html", {
                'form': form,
                "save": True
            })

    return render(request, "contact.html", {
        'form': CreateNewPageForm(),
        "save": False
    })


def skills(request):
    return render(request, "skills.html", {})
