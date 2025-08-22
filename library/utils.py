from django.utils import timezone
from decimal import Decimal
from .models import BookIssue, IssueLog

def log_overdue_and_fines():
    today = timezone.now().date()
    overdue_issues = BookIssue.objects.filter(returned=False, due_date__lt=today)

    for issue in overdue_issues:
        fine = issue.calculate_fine()
        issue.fine_amount = fine
        issue.save()

        IssueLog.objects.create(
            book_issue=issue,
            action='overdue',
            status='fine issued',
            note=f"BDT {fine} for overdue book issued to {issue.user.username}"
        )
