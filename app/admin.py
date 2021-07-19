from django.contrib import admin
from .models import BaseProfile, Manager, Patient

@admin.register(BaseProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'is_admin')
    raw_id_fields = ('user',)

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('profile', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('profile', )
