from django.contrib import admin
from .models import service, packageDetails,servicePackages
# Register your models here.

admin.site.register(service)
admin.site.register(packageDetails)
admin.site.register(servicePackages)