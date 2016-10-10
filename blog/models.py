from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class WorkOrder(models.Model):
    fix = 'fix'
    convert = 'convert'
    lte = 'lte'
    htv = 'htv'
    JOB_TYPES = ((fix, 'fix'), (convert, 'convert'), (lte, 'install/move'), (htv, 'sat install'))

    job_date = models.CharField(max_length=20)
    cust_number = models.CharField(max_length=10)
    cust_name = models.CharField(max_length=50)
    job_pay = models.IntegerField()
    pair_day = models.NullBooleanField()
    extra_charges = models.IntegerField()
    description = models.TextField()
    
    def publish(self):
        self.job_date = timezone.now()
        self.save()
        
    def calculate_commission(self):
        total = self.job_pay + self.extra_charges
        if pair_day:
            total /= 4
        else:
            total /= 2
        return total
