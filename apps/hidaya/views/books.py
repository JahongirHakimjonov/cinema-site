from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Book
from apps.hidaya.serializers import BookDetailSerializer
from apps.hidaya.serializers.books import BookSerializer
from apps.shared.pagination import CustomPagination


class BookList(APIView):
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.filter(is_active=True)
        paginator = self.pagination_class()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = self.serializer_class(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)


class BookDetail(APIView):
    serializer_class = BookDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        book = Book.objects.get(pk=pk, is_active=True)
        serializer = self.serializer_class(book, context={"request": request})
        return Response(serializer.data)
