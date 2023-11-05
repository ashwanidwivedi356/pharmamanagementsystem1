from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display = ('Doctor_name', 'Specialization', 'Openning_time', 'Closing_time','Doctor_fees')
