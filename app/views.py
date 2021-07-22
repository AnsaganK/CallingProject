from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms import PatientForm, CheckListForm
from app.models import Patient, PMSP, District, WorkType, PastIllness, AccompanyingIllnesses, RiskGroup, \
    DeregistrationCause, BadHabits, Medications, Wellbeing, DangerousSigns
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
    patients = Patient.objects.all().order_by('-pk')
    paginator = Paginator(patients, 15)
    page = request.GET.get('page')
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    return render(request, 'app/patient/list.html', {"patients": patients})

@login_required
def patients_add(request):
    if request.method == 'POST':
        print(request.POST)
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('patients')

    districts = District.objects.all()
    work_types = WorkType.objects.all()

    past_illnesses = PastIllness.objects.all()
    accompanying_illnesses = AccompanyingIllnesses.objects.all()
    risk_groups = RiskGroup.objects.all()
    bad_habits = BadHabits.objects.all()

    deregistration_causes = DeregistrationCause.objects.all()

    return render(request, 'app/patient/add.html', {'districts': districts, 'work_types': work_types,
                                                    'past_illnesses': past_illnesses, 'accompanying_illnesses': accompanying_illnesses, 'risk_groups': risk_groups, 'bad_habits': bad_habits,
                                                    'deregistration_causes': deregistration_causes
                                                    })


@login_required
def check_lists(request, pk):
    user = request.user
    patient = Patient.objects.get(pk=pk)
    check_lists = patient.check_lists.all()

    return render(request, 'app/patient/check_list.html', {'patient': patient, 'check_lists': check_lists})


@login_required
def check_lists_add(request, pk):
    patient = Patient.objects.filter(pk=pk).first()
    if not patient:
        return render(request, 'app/patient/check_list.html', {'patient': patient})
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            new_check_list = form.save(commit=False)
            new_check_list.user = request.user
            new_check_list.patient = patient
            new_check_list.save()
        else:
            print(form.errors)
        return redirect(reverse('check_lists', args=[patient.id]))
    wellbeings = Wellbeing.objects.all()
    medications = Medications.objects.all()
    dangerous = DangerousSigns.objects.all()

    return render(request, 'app/patient/check_list_add.html', {'patient': patient, 'wellbeings': wellbeings,
                                                               'medications': medications, 'dangerous': dangerous})

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
    items = model.objects.all().order_by('-pk')
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

@login_required
def medications_page(request):
    model = Medications
    title = 'Медикаменты'
    name = 'medications'
    return generate_admin_page(request, model, title, name)


@login_required
def wellbeing_page(request):
    model = Wellbeing
    title = 'Самочувствие'
    name = 'wellbeing'
    return generate_admin_page(request, model, title, name)

@login_required
def dangerous_signs_page(request):
    model = DangerousSigns
    title = 'Опасные признаки'
    name = 'dangerous_signs'
    return generate_admin_page(request, model, title, name)


class PatientDetailView(APIView):
    def get(self, request, pk, format=None):
        user = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
