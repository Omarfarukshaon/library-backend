from django.core.management.base import BaseCommand
from library.utils import log_overdue_and_fines

class Command(BaseCommand):
    help = 'Logs overdue book issues and applies fines'

    def handle(self, *args, **kwargs):
        log_overdue_and_fines()
        self.stdout.write(self.style.SUCCESS('Overdue fines logged successfully.'))
