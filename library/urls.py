from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookIssueViewSet, IssueLogViewSet, issue_book

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'book-issues', BookIssueViewSet)
router.register(r'issue-logs', IssueLogViewSet)

urlpatterns = [
    path('issue-book/', issue_book, name='issue-book'),
    path('', include(router.urls)),
]
