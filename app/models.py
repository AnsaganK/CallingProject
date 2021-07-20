from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    patronymic = models.CharField(max_length=120, default="", null=True, blank=True, verbose_name='Отчество')
    number_phone = models.CharField(max_length=250, null=True, blank=True, verbose_name='Мобильный')

    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    is_manager = models.BooleanField(default=False, verbose_name='Менеджер')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class PMSP(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ПМСП'
        verbose_name_plural = 'ПМСП'


class WorkType(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Тип работы'
        verbose_name_plural='Типы работ'


class District(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class PastIllness(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Перенесенное заболевание'
        verbose_name_plural = 'Перенесенные заболевания'


class AccompanyingIllnesses(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сопутсвуещие заболевание'
        verbose_name_plural = 'Сопутсвующие заболевания'


class RiskGroup(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа риска'
        verbose_name_plural = 'Группы риска'


class BadHabits(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вредная привычка'
        verbose_name_plural = 'Вредные привычки'


class Father(models.Model):
    first_name = models.CharField(max_length=250, default="", null=True, blank=True)
    last_name = models.CharField(max_length=250, default="", null=True, blank=True)
    patronymic = models.CharField(max_length=250, default="", null=True, blank=True)
    blood_type_choices = (
        ('1+', '1+'),
        ('2+', '2+'),
        ('3+', '3+'),
        ('4+', '4+'),
        ('1-', '1-'),
        ('2-', '2-'),
        ('3-', '3-'),
        ('4-', '4-'),
    )
    blood_type = models.CharField(max_length=250, choices=blood_type_choices, null=True, blank=True)
    work_type = models.ManyToManyField(WorkType, null=True, blank=True)
    bad_habits = models.ForeignKey(BadHabits, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Отец'
        verbose_name_plural = 'Отцы'


class DeregistrationCause(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Причина снятия'
        verbose_name_plural = 'Причины снятия'


class Patient(models.Model):
    first_name = models.CharField(max_length=250, default="", blank=True)
    last_name = models.CharField(max_length=250, default="", blank=True)
    patronymic = models.CharField(max_length=250, default="", blank=True)
    birth_date = models.DateField(null=True, blank=True)
    before_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    height = models.IntegerField(default=0, blank=True)
    blood_type_choices = (
        ('1+', '1+'),
        ('2+', '2+'),
        ('3+', '3+'),
        ('4+', '4+'),
        ('1-', '1-'),
        ('2-', '2-'),
        ('3-', '3-'),
        ('4-', '4-'),
    )
    blood_type = models.CharField(max_length=250, choices=blood_type_choices, null=True, blank=True)
    children_amount = models.IntegerField(verbose_name='Количество детей', default=0, blank=True)
    PMSP = models.ForeignKey(PMSP, on_delete=models.CASCADE, null=True, blank=True)
    IIN = models.CharField(max_length=12, default='', blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=250, blank=True, default='',)
    mobile_phone = models.CharField(max_length=250, blank=True, verbose_name='Мобильный телефон', default='')
    work_type = models.ManyToManyField(WorkType, null=True, blank=True)
    total_pregnancies = models.IntegerField(default=0, blank=True)

    past_illnesses = models.ManyToManyField(PastIllness, verbose_name='Перенесенные заболевания', null=True, blank=True)
    accompanying_illnesses = models.ManyToManyField(AccompanyingIllnesses, verbose_name='Сопутсвующие заболевания', null=True, blank=True, )
    risk_group = models.ManyToManyField(RiskGroup, null=True, blank=True, verbose_name='Группа риска')
    bad_habits = models.ManyToManyField(BadHabits, null=True, blank=True, verbose_name='Плохие привычки')

    father = models.ForeignKey(Father, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Отец')

    registration_date = models.DateField(null=True, blank=True)
    last_menstruation = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    deregistration_date = models.DateField(null=True, blank=True)
    deregistration_cause = models.ForeignKey(DeregistrationCause, on_delete=models.CASCADE, null=True, blank=True)

    comments = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"


class Wellbeing(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Самочувствие'
        verbose_name_plural = 'Самочувствие'


class Medications(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'


class CheckList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True)

    wellbeing = models.ForeignKey(Wellbeing, on_delete=models.CASCADE, verbose_name='Самочувствие')
    complaints = models.BooleanField(default=False, )
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    medications = models.ManyToManyField(Medications)

    urination_frequency = models.IntegerField()

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = 'Чек лист'
        verbose_name_plural = 'Чек листы'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()











