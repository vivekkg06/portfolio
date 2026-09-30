

# Create your views here.
from django.shortcuts import render, redirect
from .models import Profile, Service, Skill, Project, Contact


def home(request):
    profile = Profile.objects.first()
    services = Service.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        "profile": profile,
        "services": services,
        "skills": skills,
        "projects": projects,
    }

    return render(request, "portfolio/index.html", context)


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return redirect("home")

    return redirect("home")