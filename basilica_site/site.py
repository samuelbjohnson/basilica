from basilica.blocks import Page
from basilica.models import *

# the actual site

page1 = Page({
	'title': Text.objects.get(content_name='site title'),
	'contents': [
		('text', Text.objects.get(content_name='test text')),
		('paragraph', Paragraph.objects.get(content_name='Test Paragraph')),
		('ipsum', Paragraph.objects.get(content_name='Ipsum paragraph')),
		('markdown', MarkdownSection.objects.get(content_name='Test markdown'))
	]
}, base_template='basilica_site/main.html',  page_template='basilica/page.html')