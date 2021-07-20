from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from app.models import MANAGER, PATIENT


@login_required
def home(request):
    return render(request, 'app/base.html')


@login_required
def profile(request):
    user = request.user

    if user.profile.is_admin:
        return render(request, 'app/admin/profile.html', {"user": user})

    if user.profile.role == MANAGER:
        return render(request, 'app/manager/profile.html', {"user": user})

    elif user.profile.role == PATIENT:
        return render(request, 'app/patient/profile.html', {"user": user})


@login_required
def managers_list(request):
    managers = User.objects.filter(profile__role=MANAGER)
    return render(request, 'app/manager/list.html', {"managers": managers})


@login_required
def patients_list(request):
    patients = User.objects.filter(profile__role=PATIENT)
    return render(request, 'app/patient/list.html', {"patients": patients})


@login_required
def about_service(request):
    return render(request, 'app/other/about.html')

@login_required
def contacts(request):
    return render(request, 'app/other/contacts.html')