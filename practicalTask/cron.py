from django.core.mail import send_mail
from practicalTask import settings
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print('Cron Job Successfully executed!')
        subject = 'Happy Birthday'
        message = 'Happy Birthday'
        from_email = settings.EMAIL_HOST_USER
        receipent_list = ['kush@bluehole.in']
        print('****************')
        send_mail(subject, message, from_email, receipent_list)