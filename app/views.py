from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Patient, PMSP, District, WorkType, PastIllness, AccompanyingIllnesses, RiskGroup, \
    DeregistrationCause, BadHabits
from app.serializers import PatientSerializer


@login_required
def home(request):
    return render(request, 'app/base.html')


@login_required
def profile(request):
    user = request.user

    if user.profile.is_admin:
        return render(request, 'app/admin/profile.html', {"user": user})

    elif user.profile.is_manager:
        return render(request, 'app/manager/profile.html', {"user": user})


@login_required
def managers_list(request):
    managers = User.objects.filter(profile__is_manager=True)
    return render(request, 'app/manager/list.html', {"managers": managers})


@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'app/patient/list.html', {"patients": patients})


@login_required
def about_service(request):
    return render(request, 'app/other/about.html')

@login_required
def contacts(request):
    return render(request, 'app/other/contacts.html')


def generate_admin_page(request, model, title, name):
    if request.method == 'POST' and request.POST['name']:
        if 'id' in request.POST:
            item = model.objects.get(pk=int(request.POST['id']))
            item.name = request.POST['name']
            item.save()
        elif not model.objects.filter(name=request.POST['name']).first():
            new_item = model.objects.create(name=request.POST['name'])
            new_item.save()
    if 'id' in request.GET:
        id = request.GET.get('id')
        item = model.objects.filter(pk=id).first()
        if item:
            item.delete()
    items = model.objects.all()
    return render(request, 'app/admin/admin_panel.html', {"items": items, "title": title, "name": name})

@login_required
def PMSPs_page(request):
    model = PMSP
    title = 'ПМСП'
    name = 'pmsp'
    return generate_admin_page(request, model, title, name)

@login_required
def districts_page(request):
    model = District
    title = 'Районы'
    name = 'district'
    return generate_admin_page(request, model, title, name)

@login_required
def work_types_page(request):
    model = WorkType
    title = 'Тип работы'
    name = 'work_type'
    return generate_admin_page(request, model, title, name)

@login_required
def past_illnesses_page(request):
    model = PastIllness
    title = 'Перенесенные заболевания'
    name = 'past_illness'
    return generate_admin_page(request, model, title, name)


@login_required
def accompanying_illnesses_page(request):
    model = AccompanyingIllnesses
    title = 'Сопутсвующие заболевания'
    name = 'accompanying_illnesses'
    return generate_admin_page(request, model, title, name)

@login_required
def risk_groups_page(request):
    model = RiskGroup
    title = 'Группы риска'
    name = 'risk_group'
    return generate_admin_page(request, model, title, name)

@login_required
def bad_habits_page(request):
    model = BadHabits
    title = 'Плохие привычки'
    name = 'bad_habits'
    return generate_admin_page(request, model, title, name)

@login_required
def deregistration_cause_page(request):
    model = DeregistrationCause
    title = 'Причины снятия'
    name = 'deregistration_cause'
    return generate_admin_page(request, model, title, name)


class PatientDetailView(APIView):
    def get(self, request, pk, format=None):
        user = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
