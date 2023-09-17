from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import News
from django.http import JsonResponse
from .models import News




class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.first()
        return context


def get_news_data(request):
    news_data = News.objects.order_by('-created_at')[:3]

    news_list = []
    for news in news_data:
        news_dict = {
            'titleNews': news.title,
            'newsText': news.description,
            'image': news.image.url,
            'Date': news.created_at
        }
        news_list.append(news_dict)

    return JsonResponse(news_list, safe=False)
