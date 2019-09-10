from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# from django.views.generic import TemplateView

# Create your views here.
def index(request):
    # print(request.method)
    template = 'emiliano/index.html'
    context = {}
    return render(request, template, context)

# Estaba siguiendo como el tuturial y no viene esto haha ¿Para qué es?
# Es que estaba en el tuyo, pero si lo quito no importa (?)
class Index(View):
    template = 'emiliano/index.html'
    context = {'title': 'Titulo'}

    def get(self, request):
        # print('With class-based views')
        # self.context["posts"] = posts
        return render(request, self.template, self.context)

class About(View):
    template_name = "emiliano/about.html"
    context = {'title': 'About me'}

    def get(self, request):
        return render(request, self.template_name, self.context)
