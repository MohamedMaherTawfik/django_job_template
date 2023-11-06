import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from job.models import Company,Category,job
import random
from faker import Faker

def create_category(n):
    fake=Faker()
    for i in range(n):
        Category.objects.create(
            name=fake.name()
        )
    print(f"{n} category was added successufully")


def create_company(n):
    fake=Faker()
    images=['job-list1.png','job-list2.png','job-list3.png','job-list4.png']
    for i in range(n):
        Company.objects.create(
            name=fake.name(),
            website = fake.url(),
            subtitle=fake.text(),
            email=fake.email(),
            logo=f"company/{images[random.randint(0,3)]}"
        )
    print(f"{n} company was added successufully")



def create_job(n):
    fake=Faker()
    jop_type=['Fulltime','Parttime','Remote','Freelance']

    for x in range(n):
        job.objects.create(
            title=fake.name(),
            company=Company.objects.all().order_by('?')[0],
            description=fake.sentence(),
            vacancy=random.randint(1,5),
            salary_start=random.randint(2000,2500),
            salary_end=random.randint(4000,5000),
            experince=random.randint(1,3),
            category=Category.objects.all().order_by('?')[0],
            job_type=jop_type[random.randint(0,3)],
        )

    print(f"{n} job was added successufully")    





#create_company(10)
#create_category(10)
#create_job(10)