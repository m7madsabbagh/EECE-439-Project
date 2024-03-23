from django.shortcuts import render

# Create your views here.
from .forms import ContactForm 
from .models import Contacts 
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.urls import reverse


class ContactListView(ListView):
    model = Contacts
    template_name = 'contacts.html'
    context_object_name = 'contact_list'
    success_url = '/contacts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        balance_list = context[self.context_object_name]
        context[self.context_object_name] = balance_list
        return context
    
class ContactCreateView(CreateView):
    model = Contacts
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/contacts'
    def form_valid(self, form):
        balance = form.save()
        return HttpResponseRedirect(reverse('contacts'))
class ContactUpdateView(UpdateView):
    model= Contacts
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/contacts'
    
class ContactDeleteView(DeleteView):
    model = Contacts
    success_url = '/contacts'

    def get(self,request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)
 