from django.contrib import admin
from .models import ideaDetails
# Register your models here.
@admin.register(ideaDetails)
class ideaDetailsModelAdmin(admin.ModelAdmin):
    list_display=['id','businessName','businessLocation','businessType','investmentAmount','contractDuration','numberOfPeople','businessDescription']