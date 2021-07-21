from django.db import models

# Create your models here.


class Position(models.Model):
    position_title = models.CharField(max_length=250, unique=True, blank=False, verbose_name="Должность")

    def __str__(self):
        return "{}".format(self.position_title)


class Level(models.Model):
    level_title = models.CharField(max_length=250, unique=True, blank=False, verbose_name="Уровень")

    def __str__(self):
        return "{}".format(self.level_title)


class OtherInformation(models.Model):
    age = models.IntegerField(verbose_name="Возраст")
    telephone_number = models.CharField(max_length=30, verbose_name="Номер телефона")


class Chief(models.Model):
    full_name = models.CharField(max_length=250,  verbose_name="ФИО")
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name="position_chief", verbose_name="Должность")
    salary = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Зарплат")
    first_work_date = models.DateField(verbose_name="Первый рабочий день")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="level_chief", verbose_name="Уровень")
    other_information = models.OneToOneField(OtherInformation, on_delete=models.CASCADE,
                                             null=True, blank=True, related_name="chief_othr_inf",
                                             verbose_name="Прочая инофрмация")

    def __str__(self):
        return "{}".format(self.full_name)


class Employer(models.Model):
    full_name = models.CharField(max_length=250, verbose_name="ФИО")
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name="position_empl", verbose_name="Должность")
    salary = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Зарплат")
    first_work_date = models.DateField(verbose_name="Первый рабочий день")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="level_empl", verbose_name="Уровень")
    chief = models.ForeignKey(Chief, on_delete=models.CASCADE, related_name="empl_chief", verbose_name="Начальник")
    other_information = models.OneToOneField(OtherInformation, on_delete=models.CASCADE,
                                             null=True, blank=True, related_name="empl_othr_inf",
                                             verbose_name="Прочая инофрмация")
    paid_salary = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Всего выплачено")

    def __str__(self):
        return "{}".format(self.full_name)






