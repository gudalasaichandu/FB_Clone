from django.contrib import admin
from auth import models
# Register your models here.
admin.sites.register([
    models
])