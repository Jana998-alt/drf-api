from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Particle
from .serializer import ParticlesSerializer


# # Create your views here.
class ParticlesListView(generics.ListCreateAPIView):
    serializer_class = ParticlesSerializer
    queryset =  Particle.objects.all()

class ParticlesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticlesSerializer
    queryset =  Particle.objects.all()
    