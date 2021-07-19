from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse

MANAGER = 'manager'
PATIENT = 'patient'

ROLE_CHOICES = (
    (MANAGER, 'Менеджер'),
    (PATIENT, 'Пациент'),
)


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=40, choices=ROLE_CHOICES, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Основной профиль'
        verbose_name_plural = 'Основные профиля'


class Manager(models.Model):
    profile = models.ForeignKey(BaseProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='manager')
    number_phone = models.CharField(max_length=250, null=True, blank=True)
    patronymic = models.CharField(max_length=120, default="", null=True, blank=True)
    def __str__(self):
        return self.profile.user.username

    def get_absolute_url(self):
        return reverse('manager_detail', args=[str(self.profile.user.pk)])

    class Meta:
        verbose_name = "Профиль менеджера"
        verbose_name_plural = "Профили менеджеров"


class Patient(models.Model):
    profile = models.ForeignKey(BaseProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')
    patronymic = models.CharField(max_length=120, default="", null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    before_weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.IntegerField()


    blocked = models.BooleanField(default=False)
    archive = models.BooleanField(default=False, null=True, blank=True, verbose_name="Архив")

    def __str__(self):
        return self.profile.user.username

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.profile.user.pk)])

    class Meta:
        verbose_name = "Профиль пациента"
        verbose_name_plural = "Профили пациентов"


class Inspection(models.Model):
    pass

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        BaseProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()











