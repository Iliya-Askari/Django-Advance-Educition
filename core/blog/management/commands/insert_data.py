from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from accounts.models import User , Profile
from blog.models import Post , Category

class Command(BaseCommand):
    help = "Inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password='Test@123456')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()
        print(profile)
        print()
        print(profile.first_name , profile.last_name)
        print()
        print(profile.description)
        