from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    print(request.method)
    template = 'emiliano/index.html'
    context = {}
    return render(request, template, context)

# Estaba siguiendo como el tuturial y no viene esto haha ¿Para qué es?
# Es que estaba en el tuyo, pero si lo quito no importa (?)
class Index(TemplateView):
    template = 'emiliano/index.html'
    context = {'title': 'Index'}

    def get(self, request):
        print('With class-based views')
        return render(request, self.template, self.context)

class AboutView(TemplateView):
    template_name = "about.html"
    context = {'title': 'About me'}

    def get(self, request):
        return render(request, self.template_name, self.context)
