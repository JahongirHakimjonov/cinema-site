from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.hidaya.models import Video
from apps.hidaya.tasks import process_video


@receiver(post_save, sender=Video)
def video_uploaded_handler(sender, instance, created, **kwargs):
    if created:
        process_video.delay(instance.id)
