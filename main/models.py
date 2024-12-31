from django.db import models
from django.utils.text import slugify
# Create your models here.


class service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images')
    link = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.name)  # Automatically generate a slug from the name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class servicePackages(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lkr_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_popular = models.BooleanField(default=False)
    description = models.TextField()
    def __str__(self):
        return self.package_name

    

class packageDetails(models.Model):
    servicePackage = models.ForeignKey(servicePackages, on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return self.detail


