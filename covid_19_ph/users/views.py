from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView
from django.shortcuts import render

from covid_19_ph.users.covid_data import get_data, get_vaccine, get_therapeutic, get_news

User = get_user_model()

class HomeView(ListView):

    def get(self, request):
        stat_data = get_data()
        return render(request, 'pages/home.html', stat_data)


class VaccineView(ListView):

    def get(self, request):
        vaccine_data = get_vaccine()
        return render(request, 'pages/vaccine.html', vaccine_data)


class TherapeuticView(ListView):

    def get(self, request):
        tp_data = get_therapeutic()
        return render(request, 'pages/therapeutic.html', tp_data)


class NewsView(ListView):

    def get(self, request):
        article_data = get_news()
        return render(request, 'pages/news.html', article_data)


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
