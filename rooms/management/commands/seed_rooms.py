import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates rooms"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    # help="How many times do you want me to tell you that I love you"
    #     )

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many do you want to create rooms?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = users_models.User.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = rooms_models.Amenity.objects.all()
        facilities = rooms_models.Facility.objects.all()
        rules = rooms_models.HouseRule.objects.all()
        for pk in created_clean:
            room = rooms_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                rooms_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
