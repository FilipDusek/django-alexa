
from django.conf.urls import url
from .views import ASKView

urlpatterns = [
    url(r'^alexa/ask/$', ASKView.as_view(), name="alexa"),
]
