from django.contrib import admin
from .models import BookIssue
from .models import IssueLog
from .models import UserProfile

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'due_date', 'returned', 'fine_amount')
    list_filter = ('returned',)
    search_fields = ('book__title', 'user__username')


@admin.register(IssueLog)
class IssueLogAdmin(admin.ModelAdmin):
    list_display = ('book_issue', 'status', 'timestamp')
    search_fields = ('status', 'note')
    list_filter = ('status',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_borrow')
