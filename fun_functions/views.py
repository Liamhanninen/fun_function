from django.views.generic import CreateView
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers

class DefaultCreateViewWithList(CreateView):
    template_name = 'fun_functions/default_create.html'
    
    def get_success_url(self):
        return self.request.path
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = serializers.serialize( "python", self.model.objects.all().order_by('-created')) 
        context['field_names'] = self.model._meta.get_fields()[1:]
        context['model'] = self.model.__name__
        return context

class TriangleAreaView(DefaultCreateViewWithList):
    model = TriangleArea
    fields = ['base','height']

class MaximumEdgeView(DefaultCreateViewWithList):
    model = MaximumEdge
    fields = ['first_side','second_side']

class SecondsConversionView(DefaultCreateViewWithList):
    model = SecondsConversion
    fields = ['time_type','amount']

class RepeatingFunctionView(DefaultCreateViewWithList):
    model = RepeatingFunction
    fields = ['string_to_repeat','repeat_n_times']

def index(request):
    return render(request, 'fun_functions/index.html')

def help(request):
    return render(request, 'fun_functions/help.html')