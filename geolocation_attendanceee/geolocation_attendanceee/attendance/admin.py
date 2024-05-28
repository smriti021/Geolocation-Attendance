from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp')
    search_fields = ('user__username',)

admin.site.register(Attendance, AttendanceAdmin)
