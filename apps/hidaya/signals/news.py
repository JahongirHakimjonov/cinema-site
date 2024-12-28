# import logging
#
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from apps.hidaya.models import NotificationType, Notification, News
#
# logger = logging.getLogger(__name__)
#
#
# @receiver(post_save, sender=News)
# def news_signal(sender, instance, created, **kwargs):  # noqa
#     if created:
#         Notification.objects.create(
#             title_uz="Yangilik qo'shildi",
#             title_ru="Добавлено новость",
#             title_en="New news added",
#             title_uz_Cyrl="Янгилик қўшилди",
#             message_uz=f"{instance.title_uz}",
#             message_ru=f"{instance.title_ru}",
#             message_en=f"{instance.title_en}",
#             message_uz_Cyrl=f"{instance.title_uz_Cyrl}",
#             banner=instance.banner,
#             type=NotificationType.ALL,
#         )
#         logger.info(f"New book {instance.title} added.")
