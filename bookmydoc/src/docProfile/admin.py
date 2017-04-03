from django.contrib import admin

# Register your models here.
from .models import DocDetails
from .models import Locations	
from .models import BookDoc
from .models import BookDetails
from .models import EmergDoctor


# class Docdetailsadmin(admin.ModelAdmin):
# 	model = DocDetails
# 	list_display = ["doc_name,doc_location,doc_phone"]


admin.site.register(DocDetails)
admin.site.register(Locations)
admin.site.register(BookDoc)
admin.site.register(BookDetails)
admin.site.register(EmergDoctor)

