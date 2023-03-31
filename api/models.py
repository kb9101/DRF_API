from django.db import models
from django.core.mail import send_mail
from practicalTask import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Companies(models.Model):
    company_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.company_name

class Employees(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    company_id = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, null=True)
    email_address = models.EmailField(null=True)

    def __str__(self):
        return self.first_name
    
@receiver(post_save, sender=Employees)
def send_mail_on_create(sender, instance=None, created=False, **kwargs):
    if created:
        subject = 'Welcome to our website!'
        message = 'Welcome to our website!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email_address]
        send_mail(subject, message, from_email, recipient_list)