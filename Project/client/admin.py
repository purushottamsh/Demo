from django.contrib import admin
from .models import Client,CustomUser,Project

# Register your models here.

admin.site.register ( Client )
admin.site.register ( CustomUser )
admin.site.register ( Project )
