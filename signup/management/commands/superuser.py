

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    args = '<username>'
    help = 'Give the specified user superuser privilege'

    def handle(self, *args, **options):
        
        username = " ".join(args)
        
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError("User %s does not exist" % username)

        u.is_superuser = True
        u.save()
        
        self.stdout.write("%s is now a superuser" % username)

    
