from django.urls import path
from .api import api


urlpatterns = [
    path(route='api/', view=api.urls),
]
