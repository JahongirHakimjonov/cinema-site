from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="search",
                description="Search term for filtering books by title, sub title, description, or author",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="category",
                description="Category for filtering books",
                required=False,
                type=str,
            ),
        ],
        responses=BookSerializer(many=True),
    )
    def get(self, request):
        search = request.query_params.get("search")
        category = request.query_params.get("category")
        books = Book.objects.filter(is_active=True)
        if category:
            books = books.filter(category=category)
        queryset = books
        if search:
            search_terms = search[:100].split()
            query = Q()
            for term in search_terms:
                query &= (
                    Q(title__icontains=term)
                    | Q(sub_title__icontains=term)
                    | Q(description__icontains=term)
                    | Q(author__icontains=term)
                )
            queryset = books.filter(query).distinct()
        paginator = self.pagination_class()
        paginated_books = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)


class BookDetail(APIView):
    serializer_class = BookDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        book = Book.objects.get(pk=pk, is_active=True)
        serializer = self.serializer_class(book, context={"request": request})
        return Response(
            {
                "success": True,
                "message": "Book fetched successfully.",
                "data": serializer.data,
            }
        )
