from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('triangle_area', views.TriangleAreaView.as_view(), name='triangle_area'),
    path('maximum_edge', views.MaximumEdgeView.as_view(), name='maximum_edge'),
    path('seconds_conversion', views.SecondsConversionView.as_view(), name='seconds_conversion'),
    path('repeating_function', views.RepeatingFunctionView.as_view(), name='repeating_function'),
    path('help', views.help, name='help'),
]