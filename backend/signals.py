from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import InterviewScore

@receiver(post_save, sender=InterviewScore)
@receiver(post_delete, sender=InterviewScore)
def update_application_score(sender, instance, **kwargs):
    instance.application.update_avgInterviewScore()
    instance.application.save()