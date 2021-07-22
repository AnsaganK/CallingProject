from rest_framework import serializers
from . import models

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BloodTypes
        fields = ('name',)


class PMSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PMSP
        fields = ('name',)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkType
        fields = ('name',)


class PastIllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PastIllness
        fields = ('name',)


class AccompanyingIllnessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccompanyingIllnesses
        fields = ('name',)


class RiskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RiskGroup
        fields = ('name',)


class BadHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BadHabits
        fields = ('name',)


class FatherSerializer(serializers.ModelSerializer):
    work_type = WorkTypeSerializer(many=True)
    bad_habits = WorkTypeSerializer(many=True)
    blood_type = BloodTypeSerializer()
    class Meta:
        model = models.Father
        fields = '__all__'

class DeregistrationCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeregistrationCause
        fields = ('name',)


class PatientSerializer(serializers.ModelSerializer):
    blood_type = BloodTypeSerializer()
    PMSP = PMSPSerializer()
    work_type = WorkTypeSerializer(many=True)
    past_illnesses = WorkTypeSerializer(many=True)
    accompanying_illnesses = WorkTypeSerializer(many=True)
    risk_group = WorkTypeSerializer(many=True)
    bad_habits = WorkTypeSerializer(many=True)
    father = FatherSerializer()
    deregistration_cause = DeregistrationCauseSerializer()
    class Meta:
        model = models.Patient
        fields = '__all__'