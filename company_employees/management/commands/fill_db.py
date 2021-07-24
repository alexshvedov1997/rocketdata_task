from django.core.management.base import BaseCommand
from company_employees.models import OtherInformation
from django_seed import Seed
import random


class Command(BaseCommand):
    help = "Add 3 massage to OtherInformation"

    def handle(self, *args, **options):
        print("Seed check work")

        seeder = Seed.seeder()
        seeder.add_entity(OtherInformation, 10,{
            'age': lambda x: random.randint(18, 70),
            'telephone_number': lambda x: self.__create_telephone_number()
        })
        seeder.execute()


    def __create_telephone_number(self):
        start_number = ("+37525", "+37544", "+37529")
        list_num = [str(elem) for elem in range(10)]
        random.shuffle(list_num)
        return start_number[random.randint(0, 2)] + ''.join(list_num[:7])
