from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.db import transaction

from .models import Book, BookIssue, IssueLog
from .serializers import BookSerializer, BookIssueSerializer, IssueLogSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

class BookIssueViewSet(viewsets.ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            book_issue = serializer.save()
            IssueLog.objects.create(
                book_issue=book_issue,
                action='issued',
                status='book issued',
                note=f"Issued to {book_issue.user.username}",
                timestamp=timezone.now()
            )

class IssueLogViewSet(viewsets.ModelViewSet):
    queryset = IssueLog.objects.all()
    serializer_class = IssueLogSerializer

@api_view(['POST'])
def issue_book(request):
    data = request.data

    try:
        book = Book.objects.select_for_update().get(id=data['book_id'])
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    if not book.available:
        return Response({'error': 'Book is currently unavailable'}, status=400)

    serializer = BookIssueSerializer(data=data)
    if serializer.is_valid():
        with transaction.atomic():
            book_issue = serializer.save()
            book.available = False
            book.save()

            IssueLog.objects.create(
                book_issue=book_issue,
                action='issued',
                status='book issued',
                note=f"Issued to {book_issue.user.username}",
                timestamp=timezone.now()
            )
        return Response({'message': 'Book issued and log created successfully'})
    return Response(serializer.errors, status=400)

