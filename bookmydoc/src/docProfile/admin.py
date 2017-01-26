from django.contrib import admin

# Register your models here.
from .models import DocDetails
from .models import Locations	


# class Docdetailsadmin(admin.ModelAdmin):
# 	model = DocDetails
# 	list_display = ["doc_name,doc_location,doc_phone"]


admin.site.register(DocDetails)
admin.site.register(Locations)
