from django.contrib import admin
from application3.models import reporters
from application3.models import article
class reporters_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','p1','p2','email']
admin.site.register(reporters,reporters_admin)
class article_admin(admin.ModelAdmin):
    list_display=['headlines','publice_date','reporters']
admin.site.register(article,article_admin)