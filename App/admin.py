from django.contrib import admin
from .models import VisitorFeedback

@admin.register(VisitorFeedback)
class VisitorFeedbackAdmin(admin.ModelAdmin):
    list_display = ['overall_experience', 'created_at']
    list_filter = ['overall_experience', 'visit_date', 'created_at']
    search_fields = ['name', 'email', 'comments']
