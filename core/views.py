from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """Retorna el template home"""
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi super Web Playground'})

class SamplePageView(TemplateView):
    """Retorna el template sample"""
    template_name = "core/sample.html"
