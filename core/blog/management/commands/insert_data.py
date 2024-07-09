from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from datetime import datetime
import random
from accounts.models import User , Profile
from blog.models import Post , Category


category_list = [
    "Technology",
    "Sports",
    "Politics",
    "Business",
    "Health",
    "Science",
    "World",
    "Travel"
]
class Command(BaseCommand):
    help = "Inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        profiles = []
        for _ in range(10):
            user = User.objects.create_user(email=self.fake.email(), password='Test@123456')
            profile = Profile.objects.get(user=user)
            profile.first_name = self.fake.first_name()
            profile.last_name = self.fake.last_name()
            profile.description = self.fake.paragraph(nb_sentences=3)
            profile.save()
            profiles.append(profile)
        
        for name in category_list:
            Category.objects.get_or_create(name=name)
        
        for _ in range(10):
            Post.objects.create(
                author = random.choice(profiles),
                title = self.fake.paragraph(nb_sentences=1),
                content = self.fake.paragraph(nb_sentences=5),
                status = self.fake.boolean(),
                category = Category.objects.get(name=self.fake.random_element(category_list)),
                published_date = datetime.now()
            )