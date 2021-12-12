from rest_framework import serializers
from .models import Particle

class ParticlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name', 'charge', 'type')
        model = Particle