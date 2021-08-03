from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, AticleDetails

urlpatterns = [
    # path('article/', article_list), function based
    path('article/', ArticleAPIView.as_view()), #Class based
    # path('detail/<int:pk>', article_detail), function based
    path('detail/<int:id>', AticleDetails.as_view()), #Class based
]
