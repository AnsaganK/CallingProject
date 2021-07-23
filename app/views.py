from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms import PatientForm, CheckListForm, ManagerForm, UserEditForm, ProfileEditForm
from app.models import Patient, PMSP, District, WorkType, PastIllness, AccompanyingIllnesses, RiskGroup, \
    DeregistrationCause, BadHabits, Medications, Wellbeing, DangerousSigns, CheckList, BloodTypes, Father
from app.serializers import PatientSerializer


@login_required
def home(request):
    return render(request, 'app/base.html')


@login_required
def profile(request):
    user = request.user
    return render(request, 'app/profile/profile.html', {"user": user})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form1 = UserEditForm(request.POST, instance=request.user)
        form2 = ProfileEditForm(request.POST, instance=request.user.profile)
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        return redirect(reverse('profile'))
    return render(request, 'app/profile/profile_edit.html')

@login_required
def managers_list(request):
    managers = User.objects.filter(profile__is_manager=True)
    return render(request, 'app/manager/list.html', {"managers": managers})

@login_required
def managers_add(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            new_manager = form.save()
            new_manager.profile.patronymic = request.POST['patronymic']
            new_manager.profile.is_manager = True
            new_manager.save()
        else:
            print(form.errors)
        return redirect(reverse('managers_list'))
    return render(request, 'app/manager/add.html')

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
def created_check_lists(request):
    check_lists = CheckList.objects.filter(user=request.user).order_by('-pk')
    paginator = Paginator(check_lists, 10)
    page = request.GET.get('page')
    try:
        check_lists = paginator.page(page)
    except PageNotAnInteger:
        check_lists = paginator.page(1)
    except EmptyPage:
        check_lists = paginator.page(paginator.num_pages)
    return render(request, 'app/manager/check_lists.html', {'check_lists': check_lists})


def save_many_to_many(data, field_name, model, object):
    for i in data:
        if i == field_name:
            for j in data[i]:
                item = model.objects.filter(id=int(j)).first()
                if item:
                    object.add(item)

def create_father(data):
    first_name = data['father_first_name'][0] if data['father_first_name'] else ''
    last_name = data['father_last_name'][0] if data['father_last_name'] else ''
    patronymic = data['father_patronymic'][0] if data['father_patronymic'] else ''
    comments = data['father_comments'][0] if data['father_comments'] else ''
    father = Father.objects.create(first_name=first_name, last_name=last_name, patronymic=patronymic,
                                   comments=comments,
                                   )
    if data['father_blood_type']:
        blood_type = BloodTypes.objects.filter(id=int(data['father_blood_type'][0])).first()
        father.blood_type = blood_type
    father.save()
    save_many_to_many(data, 'father_bad_habits', BadHabits, father.bad_habits)
    save_many_to_many(data, 'father_work_type', WorkType, father.work_type)

    return father


@login_required
def patients_add(request):
    if request.method == 'POST':
        data = dict(request.POST)
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save()
            save_many_to_many(data, 'work_type', WorkType, new_patient.work_type)
            save_many_to_many(data, 'past_illnesses', PastIllness, new_patient.past_illnesses)
            save_many_to_many(data, 'accompanying_illnesses', AccompanyingIllnesses, new_patient.accompanying_illnesses)
            save_many_to_many(data, 'risk_group', RiskGroup, new_patient.risk_group)
            save_many_to_many(data, 'bad_habits', BadHabits, new_patient.bad_habits)
            new_patient.father = create_father(data)
            new_patient.save()
        else:
            print(form.errors)
        return redirect(reverse('patients_list'))

    PMSPs = PMSP.objects.all()
    districts = District.objects.all()
    work_types = WorkType.objects.all()

    past_illnesses = PastIllness.objects.all()
    accompanying_illnesses = AccompanyingIllnesses.objects.all()
    risk_groups = RiskGroup.objects.all()
    blood_types = BloodTypes.objects.all()
    bad_habits = BadHabits.objects.all()

    deregistration_causes = DeregistrationCause.objects.all()

    return render(request, 'app/patient/add.html', {'districts': districts, 'work_types': work_types, 'PMSPs': PMSPs, 'blood_types': blood_types,
                                                    'past_illnesses': past_illnesses, 'accompanying_illnesses': accompanying_illnesses, 'risk_groups': risk_groups, 'bad_habits': bad_habits,
                                                    'deregistration_causes': deregistration_causes
                                                    })


@login_required
def check_lists(request, pk):
    user = request.user
    patient = Patient.objects.get(pk=pk)
    check_lists = patient.check_lists.order_by('-pk').all()
    paginator = Paginator(check_lists, 10)
    page = request.GET.get('page')
    try:
        check_lists = paginator.page(page)
    except PageNotAnInteger:
        check_lists = paginator.page(1)
    except EmptyPage:
        check_lists = paginator.page(paginator.num_pages)
    return render(request, 'app/patient/check_list.html', {'patient': patient, 'check_lists': check_lists})

@login_required
def check_list_detail(request, pk):
    check_list = CheckList.objects.filter(id=pk).first()
    if not check_list:
        return redirect(reverse('created_check_lists'))

    wellbeings = Wellbeing.objects.all()
    medications = Medications.objects.all()
    dangerous = DangerousSigns.objects.all()
    return render(request, 'app/patient/check_list_detail.html', {'check_list': check_list, 'wellbeings': wellbeings,
                                                               'medications': medications, 'dangerous': dangerous})

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
            for i in request.POST:
                if 'dangerous_sign_' in i:
                    dangerou_id = int(i.split('_')[2])
                    dangerous_sign = DangerousSigns.objects.filter(pk=dangerou_id).first()
                    if dangerous_sign:
                        new_check_list.dangerous_signs.add(dangerous_sign)
                if i == 'medications':
                    for j in dict(request.POST)[i]:
                        medication_id = int(j)
                        medication = Medications.objects.filter(id=medication_id).first()
                        if medication:
                            new_check_list.medications.add(medication)
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
def blood_types_page(request):
    model = BloodTypes
    title = 'Группы крови'
    name = 'blood_types'
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
