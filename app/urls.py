from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('patients', views.patients_list, name='patients_list'),
    path('patients/add', views.patients_add, name='patients_add'),
    path('patients/<int:pk>/check_lists/', views.check_lists, name='check_lists'),
    path('patients/<int:pk>/check_lists/add', views.check_lists_add, name='check_lists_add'),
    path('managers', views.managers_list, name='managers_list'),
    path('managers/add', views.managers_add, name='managers_add'),
    path('managers/my/check-lists', views.created_check_lists, name='created_check_lists'),
    path('about', views.about_service, name='about_service'),
    path('contacts', views.contacts, name='contacts'),
]

urlpatterns += [
    path('admin/PMSP', views.PMSPs_page, name='PMSP_page'),
    path('admin/district', views.districts_page, name='district_page'),
    path('admin/work_types', views.work_types_page, name='work_type_page'),
    path('admin/past_illnesses', views.past_illnesses_page, name='past_illnesses_page'),
    path('admin/accompanying_illnesses', views.accompanying_illnesses_page, name='accompanying_illnesses_page'),
    path('admin/risk_group', views.risk_groups_page, name='risk_group_page'),
    path('admin/blood_types', views.blood_types_page, name='blood_types_page'),
    path('admin/bad_habits', views.bad_habits_page, name='bad_habits_page'),
    path('admin/deregistration_cause', views.deregistration_cause_page, name='deregistration_cause_page'),
    path('admin/medications', views.medications_page, name='medications_page'),
    path('admin/wellbeing', views.wellbeing_page, name='wellbeing_page'),
    path('admin/dangerous_signs', views.dangerous_signs_page, name='dangerous_signs_page'),
]

urlpatterns += [
    path('api/patient/<int:pk>', views.PatientDetailView.as_view(), name='PatientDetailView')
]