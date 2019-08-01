from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ActorModel
from . serializers import actorsSerializer

# Create your views here.
class actorlist(APIView):
	def get(self,request):
		actor1=ActorModel.objects.all()
		seriaizer=actorsSeriaizer(actor1,many=True)
		return Response(seriaizer.data)

	def post(self):
		pass
