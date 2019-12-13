import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','testproject.settings')
import django
django.setup()
##
import random
from basicapp.models import user_data
from faker import Faker
fakegan=Faker()
def populate(N=10):
    for entry in range(N):
        name=fakegan.name().split(" ")
        fake_first_name=name[0]
        fake_last_name=name[1]
        fake_email=fakegan.email()
        user=user_data.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
if __name__=="__main__":
    print("scripting...")
    populate()
    print("population compelted...")
