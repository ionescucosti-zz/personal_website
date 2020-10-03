from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request)
    # print(request.user)
    # return HttpResponse("<hi1>Home Page</h1>")
    return render(request, "index.html",{})


def resume_view(request, *args, **kwargs):
    return render(request, "resume.html", {})


def projects_view(request, *args, **kwargs):
    return render(request, "projects.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
