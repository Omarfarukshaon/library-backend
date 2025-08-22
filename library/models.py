from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))

    def is_overdue(self):
        return not self.returned and timezone.now().date() > self.due_date

    def calculate_fine(self):
        if self.is_overdue():
            days_late = (timezone.now().date() - self.due_date).days
            return Decimal(days_late) * Decimal('5.00')
        return Decimal('0.00')

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"


class IssueLog(models.Model):
    ACTION_CHOICES = [
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]

    book_issue = models.ForeignKey(BookIssue, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, default='issued')
    status = models.CharField(max_length=50)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.action} - {self.book_issue} @ {self.timestamp}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_borrow = models.BooleanField(default=True)

    def check_borrowing_eligibility(self):
        overdue_issues = BookIssue.objects.filter(
            user=self.user,
            returned=False,
            due_date__lt=timezone.now().date()
        )
        self.can_borrow = not overdue_issues.exists()
        self.save()

    def __str__(self):
        return f"{self.user.username} - Eligible: {self.can_borrow}"
