from django.conf.urls import url,include
from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.process_form),
    url(r'^result$', views.display_result)
]
