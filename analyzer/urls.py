from django.contrib import admin
from django.urls import path,re_path,include

from . import views

from django.views.generic import TemplateView

#from .views import MyView

urlpatterns = [
path('', views.hello_home,name='hello_myapp' ),
path('crud/', views.crudops,name='crudops' ),
path('add/', views.rti_add,name='add' ),
path(r'connection/',TemplateView.as_view(template_name = 'login.html')),
path(r'login/', views.login, name = 'login'),
path(r'signoff/',TemplateView.as_view(template_name = 'signoff_form.html')),

path(r'signoffed/', views.signoffed, name = 'signoffed'),
path(r'signedoff/', views.signoffed, name = 'signoffed'),
path(r'signout/', views.signout, name = 'signout'),
path(r'drop/', views.labeldrop, name = 'labeldrop'),
path(r'status/', views.labelstatus, name = 'labelstatus'),

path('about/', views.MyView.as_view()), # Class based
path('create/', views.RtiCreate.as_view()),
path('list/', views.RtiList.as_view()),
path('<pk>/detail', views.RtiDetailView.as_view()),
path('<pk>/update',views.RtiUpdateView.as_view()),
path('<id>/delete', views.RtiDeleteView,name="id" ),
path('form', views.RtiFormView.as_view()),

]