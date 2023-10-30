from django.contrib import admin
from .models import job,Category,Company

class jobAdmin(admin.ModelAdmin):
    list_display=['title','location','company','job_type','vacancy','category']
    search_fields=['title','category','description']
    list_filter=['vacancy','job_type','category','experince']




admin.site.register(job,jobAdmin)
admin.site.register(Category)
admin.site.register(Company)