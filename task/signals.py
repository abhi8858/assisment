from django.dispatch import receiver

from defender import signals

@receiver(signals.username_block)
def username_blocked(username, **kwargs):
    print("%s was blocked!" % username)