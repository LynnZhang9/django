from django.urls import path
from django.conf.urls import url

from .views import SimpleCandlestickWithPandas
from .views import dash_example_1_view
from .views import session_state_view


urlpatterns = [

    path('dashboard', SimpleCandlestickWithPandas.as_view(),name='simple-candlestick'),
    #path('^demo-six', dash_example_1_view, name="demo-six"),
    #path('^demo-six', dash_example_1_view, name="demo-six"),

    
]