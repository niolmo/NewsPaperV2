from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers


@receiver(post_save, sender=MailModel)
def notify_managers_mail(sender, instance, created, **kwargs):
    # в зависимости от того, есть ли такой объект уже в базе данных или нет, тема письма будет разная
    if created:
        subject = f'{instance.user_name} {instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'MailModel changed for {instance.user_name} {instance.date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )
