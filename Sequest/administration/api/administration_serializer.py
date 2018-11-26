from rest_framework import serializers
from administration.models import ReportedRequest


class ReportedRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedRequest
        fields = '__all__'
