from django.db import models



class Report(models.Model):
    def image_upload_to(instance, filename):
        return f"lost/{instance.report.id}/{filename}"
    name = models.CharField(max_length=100)
    id = models.CharField(max_length = 8, primary_key=True)
    email = models.EmailField()
    images = models.ImageField(upload_to=image_upload_to)
