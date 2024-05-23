import os
import django
from asgiref.sync import sync_to_async
# Set the default environment variable for the Django settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
django.setup()
from web.app import models


@sync_to_async
def get_or_create_user(user_id: int, telegram_id: int, username: str, first_name: str, last_name: str):
    # user, created = models.User.objects.get_or_create(
    #     user_id=user_id,
    #     telegram_id=telegram_id,
    #     username=username,
    #     first_name=first_name,
    #     last_name=last_name
    # )
    # return user, created
    pass