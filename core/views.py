from django.shortcuts import render


def index(request):
    return render(request, "core/index.html", {})

def about(request):
    return render(request, "core/about.html", {})

def jobs(request):
    return render(request, "core/job-list.html", {})

def pages(request):
    return render(request, "core/job-detail.html", {})

def contact(request):
    return render(request, "core/contact.html", {})

def post_a_job(request):
    return render(request, "core/index.html", {})
