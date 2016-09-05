from django.contrib import admin
from .models import Text, Paragraph, MarkdownSection

# Register your models here.


@admin.register(Text, Paragraph, MarkdownSection)
class ContentAdmin(admin.ModelAdmin):
	date_hierarchy = 'last_updated'
	list_display = ['content_name', 'last_updated', 'content_value']

# admin.site.register(Text)
# admin.site.register(Paragraph)
# admin.site.register(MarkdownSection)