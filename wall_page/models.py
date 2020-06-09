from django.db import models

# Create your models here.
class JobManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 3:
            errors['title'] = 'Title should be at least 3 character.'
        if len(post_data['location']) < 3:
            errors['location'] = 'A location must be provided.'
        if len(post_data['description']) < 1:
            errors['description'] = 'Description should be at least 3 character.'

        return errors




class Job(models.Model):
    title = models.CharField(max_length=55)
    location = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()