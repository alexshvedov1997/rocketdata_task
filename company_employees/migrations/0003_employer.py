# Generated by Django 3.2.5 on 2021-07-21 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_employees', '0002_alter_chief_other_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Зарплат')),
                ('first_work_date', models.DateField(verbose_name='Первый рабочий день')),
                ('paid_salary', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Всего выплачено')),
                ('chief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empl_chief', to='company_employees.chief')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_empl', to='company_employees.level', verbose_name='Уровень')),
                ('other_information', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empl_othr_inf', to='company_employees.otherinformation', verbose_name='Прочая инофрмация')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_empl', to='company_employees.position', verbose_name='Должность')),
            ],
        ),
    ]
