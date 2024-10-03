
from django.core.management.base import BaseCommand

from main import send_mail


class Common(BaseCommand):
    help = 'Send CI notification'

    def handle(self, *args, **options):
        send_mail('Test mail', 'this is a test email', 'ezozaxolmamatova905@gmail.com',
                  ['xolmamatovaezoza1@gmail.com'], fail_silently=False)
        self.stdout.write(self.style.SUCCESS("email junatildi!"))
