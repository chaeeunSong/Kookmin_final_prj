from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class AccountCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy("mvtapp:detail")
    success_url = reverse_lazy("accountapp:login")
    template_name = 'accountapp/create.html'
    context_object_name = 'objUser'


class AccountDetailView(generic.DetailView):
    pass


class AccountUpdateView(generic.UpdateView):
    pass


class AccountDeleteView(generic.DeleteView):
    pass
