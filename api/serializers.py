from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "students_id", "name", "branch"]

    