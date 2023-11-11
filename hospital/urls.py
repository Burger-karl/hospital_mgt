from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('index/', views.Index, name='dashboard'),
    
    path('view_doctor/', views.View_Doctor, name='view_doctor'),
    path('add_doctor/', views.Add_Doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)/', views.Delete_Doctor, name='delete_doctor'),

    path('view_patient/', views.View_Patient, name='view_patient'),
    path('add_patient/', views.Add_Patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)/', views.Delete_Patient, name='delete_patient'),

    path('view_appointment/', views.View_Appointment, name='view_appointment'),
    path('add_appointment/', views.Add_Appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)/', views.Delete_Appointment, name='delete_appointment'),
    
    path('admin_login/', views.Login, name='admin_login'),
    path('logout_admin/', views.Logout, name='logout_admin'),
]
