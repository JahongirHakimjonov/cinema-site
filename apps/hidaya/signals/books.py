# import logging
#
# from django.db.models.signals import post_save
# # from django.dispatch import receiver
# #
# # from apps.hidaya.models import Book, NotificationType, Notification
# #
# # logger = logging.getLogger(__name__)
# #
# #
# # @receiver(post_save, sender=Book)
# # def book_signal(sender, instance, created, **kwargs):  # noqa
# #     if created:
# #         Notification.objects.create(
# #             title_uz="Yangi kitob qo'shildi",
# #             title_ru="Добавлено новое книга",
# #             title_en="New book added",
# #             title_uz_Cyrl="Янги китоб қўшилди",
# #             message_uz=f"{instance.title_uz}",
# #             message_ru=f"{instance.title_tr}",
# #             message_en=f"{instance.title_en}",
# #             message_uz_Cyrl=f"{instance.title_uz_Cyrl}",
# #             banner=instance.banner,
# #             type=NotificationType.ALL,
# #         )
# #         logger.info(f"New book {instance.title} added.")
