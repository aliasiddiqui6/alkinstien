from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.contact_form_submission, name='index'),
    path('contact/', views.contact_form_submission, name='contact'),
    # path('login/', CustomLoginView.as_view(), name='login'),
]