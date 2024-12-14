from django.urls import path

from apps.hidaya.views import (
    PaymeCallBackAPIView,
    OrderCreate,
    BookList,
    BookDetail,
    NewsDetail,
    NewsList,
    InfoList,
    InfoDetail,
    BookCategoryList,
    NewsCategoryList,
    VideoCategoryList,
    VideoList,
    VideoDetail,
)

urlpatterns = [
    path("merchant/payme/", PaymeCallBackAPIView.as_view(), name="payme-callback"),
    path("order/", OrderCreate.as_view(), name="order-create"),
    path("book/", BookList.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book-detail"),
    path("news/", NewsList.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetail.as_view(), name="news-detail"),
    path("video/", VideoList.as_view(), name="video-list"),
    path("video/<int:pk>/", VideoDetail.as_view(), name="video-detail"),
    path("info/", InfoList.as_view(), name="info-list"),
    path("info/<int:pk>/", InfoDetail.as_view(), name="info-detail"),
    path("category/book/", BookCategoryList.as_view(), name="category-book-list"),
    path("category/news/", NewsCategoryList.as_view(), name="category-news-list"),
    path("category/video/", VideoCategoryList.as_view(), name="category-video-list"),
]
