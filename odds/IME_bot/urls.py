from django.urls import path
from . import views
from .management.commands import direct_csp, abs

urlpatterns = [
    path('', views.ime_bot, name='bot_here'),
    path('abc/', views.get, name='west'),
    path('whatsapp/', views.whatsapp, name='whatbot'),
    path('csp/', direct_csp.string, name='csp'),
    path('whatAI/', abs.watbot, name='whatAI' )

]
