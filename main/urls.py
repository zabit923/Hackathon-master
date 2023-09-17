from django.urls import path
from .views import IndexView, get_news_data


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('get_news_data/', get_news_data, name='get_news_data'),
]