from django.urls import path
from . import views 

urlpatterns = [
    path('contacts', views.ContactListView.as_view(),name='contacts'),
    path('create/', views.ContactCreateView.as_view(),name='createContact'),
    path('update/<int:pk>/',views.ContactUpdateView.as_view(),name='updateContact'),
    path('delete/<int:pk>/',views.ContactDeleteView.as_view(),name='deleteContact'),
]
