from django.contrib import admin
from . models import jobCategoryModel,jobCircularModel,jobApplicationModel

# Register your models here.
class jobCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category',)}

class jobCircularAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'post_date', 'last_date', 'vacancy', 'salary']

class jobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job_circular', 'skills', 'coverletter']

admin.site.register(jobCategoryModel,jobCategoryAdmin)
admin.site.register(jobCircularModel,jobCircularAdmin)
admin.site.register(jobApplicationModel,jobApplicationAdmin)