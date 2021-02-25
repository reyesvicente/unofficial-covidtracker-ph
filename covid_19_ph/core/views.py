from django.shortcuts import render
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from covid_19_ph.core.covid_data import get_data, get_vaccine, get_therapeutic, get_news


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