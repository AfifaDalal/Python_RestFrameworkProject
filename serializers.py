from .models import StudentModel
from rest_framework import serializers

class studentserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = StudentModel
		fields = '__all__'