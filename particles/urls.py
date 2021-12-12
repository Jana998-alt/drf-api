from django.urls import path

from .views import ParticlesListView, ParticlesDetailsView

urlpatterns = [
    path('', ParticlesListView.as_view(), name = "list_of_particles"),
    path('api/v1/particle/<int:pk>', ParticlesDetailsView.as_view(), name = "detail_particle"),
    ]