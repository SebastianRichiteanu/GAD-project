from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from tabulate import tabulate


class Command(BaseCommand):
    help = "Print all users in console."

    def handle(self, *args, **options):
        users = get_user_model().objects.all()
        users_list = []
        for user in users:
            users_list.append([user.username, user.email, user.is_superuser])
        print(tabulate(users_list, headers=['Username', 'Email', 'Is Superuser']))
