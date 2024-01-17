from django.urls import path
from . import views
# from .views import proxy_font

urlpatterns = [
    path("", views.index, name="index"),
    # path('proxy-font/<path:font_filename>/', proxy_font, name='proxy-font'),
]
