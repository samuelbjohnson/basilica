from basilica.blocks import Page, SiteMap, Menu
from basilica.models import *

# the actual site

page1 = Page({
	'name': 'Main',
	'site_title': Text.objects.get(content_name='site title'),
	'contents': [
		('text', Text.objects.get(content_name='test text')),
		('paragraph', Paragraph.objects.get(content_name='Test Paragraph')),
		('ipsum', Paragraph.objects.get(content_name='Ipsum paragraph')),
		('markdown', MarkdownSection.objects.get(content_name='Test markdown'))
	]
}, base_template='basilica_site/main.html', page_template='basilica/page.html')

page2 = Page({
	'name': 'Page 2',
	'contents': [
		('text', Text.objects.get(content_name='test text')),
		('markdown', MarkdownSection.objects.get(content_name='Test markdown'))
	]
}, base_template='basilica_site/main.html', page_template='basilica/page.html')

site_map = SiteMap([
	(r'^page1$', page1, 'page1'),
	(r'^page2$', page2, 'page2')
])

main_menu = Menu(site_map)

page1.insertContent(0, 'menu', main_menu)

