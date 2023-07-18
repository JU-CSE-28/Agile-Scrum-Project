from django.urls import path
from django.views.generic import TemplateView

app_name = 'courses'

urlpatterns = [
    path('my-page/', TemplateView.as_view(template_name='courses/template/practice.html'), name='my-page'),
]
