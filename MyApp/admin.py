from django.contrib import admin
from .models import Employee
# from .models import Profile


# Register your models here.



# class ProfileAdmin(admin.ModelAdmin):
#     list_display=['id','name','picture']
# admin.site.register(Profile,ProfileAdmin)

admin.site.register(Employee)