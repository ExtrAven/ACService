from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    image = models.ImageField(upload_to="services")

    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.service.name
