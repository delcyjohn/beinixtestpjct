from rest_framework import serializers
from . models import  ActorModel

class actorsSerializer(serializers.ModelSerializer):
	class Meta:
		model= ActorModel
		fields=('Event','Actor')
		fields= '__all__'