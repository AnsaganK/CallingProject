from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('patients', views.patients_list, name='patients_list'),
    path('managers', views.managers_list, name='managers_list'),
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
    path('admin/bad_habits', views.bad_habits_page, name='bad_habits_page'),
    path('admin/deregistration_cause', views.deregistration_cause_page, name='deregistration_cause_page'),
]

urlpatterns += [
    path('api/patient/<int:pk>', views.PatientDetailView.as_view(), name='PatientDetailView')
]