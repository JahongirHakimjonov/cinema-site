import random

from django.core.management.base import BaseCommand
from faker import Faker
from apps.users.models import User

from apps.findsport.models import Club
from apps.findsport.models import Sport, Contact, Media
from apps.shared.enums import StatusChoice


class Command(BaseCommand):
    help = "Generate fake clubs"

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = list(User.objects.all())
        sports = list(Sport.objects.all())
        contacts = list(Contact.objects.all())
        medias = list(Media.objects.all())

        for _ in range(10000):  # Generate 10000 fake clubs
            user = random.choice(users)
            sport = random.choice(sports)
            club = Club.objects.create(
                user=user,
                title=fake.company(),
                description=fake.text(),
                address=fake.address(),
                longitude=fake.longitude(),
                latitude=fake.latitude(),
                is_active=fake.boolean(),
                status=random.choice(
                    [StatusChoice.ACTIVE, StatusChoice.PENDING, StatusChoice.REJECTED]
                ),
                sport=sport,
                price=fake.pydecimal(left_digits=50, right_digits=2, positive=True),
            )
            club.contacts.set(
                random.sample(contacts, min(len(contacts), 3))
            )  # Assign up to 3 random contacts
            club.medias.set(
                random.sample(medias, min(len(medias), 3))
            )  # Assign up to 3 random medias
            club.save()
            self.stdout.write(self.style.SUCCESS(f"Generated club {club.title}"))

        self.stdout.write(self.style.SUCCESS("Successfully generated fake clubs"))
