from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Particle
from .serializer import ParticlesSerializer
from .permissions import IsAuthorOrReadOnly

# # Create your views here.
class ParticlesListView(generics.ListCreateAPIView):
    serializer_class = ParticlesSerializer
    queryset =  Particle.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

class ParticlesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticlesSerializer
    queryset =  Particle.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

