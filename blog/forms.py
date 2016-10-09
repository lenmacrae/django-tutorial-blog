from django import forms
from django.utils import timezone
from .models import Post
from .models import WorkOrder

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class  JobForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('job_date', 'cust_number', 'cust_name', 'job_type', 'description', 'extra_charges')
