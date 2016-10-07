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

    job_date = models.DateTimeField(blank=True, null=True)
    cust_number = models.CharField(max_length=10)
    cust_name = models.CharField(max_length=50)
    job_type = models.CharField(max_length=10, choices=JOB_TYPES)
    pair_day = models.BooleanField(required=false)
    extra_charges = models.DecimalField()
    description = models.TextField()
    
