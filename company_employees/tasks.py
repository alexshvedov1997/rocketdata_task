from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from .models import Employer


@periodic_task(run_every=(crontab(minute='*/5')), name='add_salary_empl')
def add_salary_empl():
    obj_empl = Employer.objects.get(id=1)
    obj_empl.paid_salary=obj_empl.paid_salary+obj_empl.salary
    obj_empl.save()




