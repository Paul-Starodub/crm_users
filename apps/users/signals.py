from django.dispatch import receiver
from djoser.signals import user_registered, user_activated, user_updated


@receiver(user_registered)
def create_profile(sender, user, request, **kwargs):
    print("Hello, new user!")


@receiver(user_activated)
def send_welcome_email(sender, user, request, **kwargs):
    print("Welcome email sent to new user!")


@receiver(user_updated)
def update_user(sender, user, request, **kwargs):
    print("User updated!")
