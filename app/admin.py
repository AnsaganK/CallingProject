from django.contrib import admin
from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin')
    raw_id_fields = ('user',)


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', )


admin.site.register(models.PMSP)
admin.site.register(models.WorkType)
admin.site.register(models.AccompanyingIllnesses)
admin.site.register(models.BadHabits)
admin.site.register(models.CheckList)
admin.site.register(models.DeregistrationCause)
admin.site.register(models.District)
admin.site.register(models.Father)
admin.site.register(models.Medications)
admin.site.register(models.PastIllness)
admin.site.register(models.RiskGroup)
admin.site.register(models.Wellbeing)
admin.site.register(models.DangerousSigns)