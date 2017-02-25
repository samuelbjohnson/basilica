from django.template import loader, TemplateDoesNotExist
from django.views.generic import View
from django.http import HttpResponse
from django.conf.urls import url
from django.core.urlresolvers import reverse

# Additional non-content-centric building blocks

class Page(View):
	def __init__(self, context, base_template='basilica/base.html', page_template='basilica/page.html'):
		super(Page, self).__init__()
		self.page_template = page_template
		self.context = context
		self.context['parent_template'] = base_template

		try:
			self.loaded_template = loader.get_template(self.page_template)
		except TemplateDoesNotExist:
			self.loaded_template = loader.get_template('basilica/page.html')

	def insertContent(self, index, name, content):
		if self.context['contents']:
			self.context['contents'].insert(index, (name, content))

	def get(self, request):
		return HttpResponse(self.loaded_template.render(self.context, request))

	def name(self):
		return self.context['name']


class SiteMap:
	# entries should be a list of (url_pattern, page, name) tuples
	def __init__(self, entries):
		self.entries = entries
		self.urlpatterns = [url(pattern, page.dispatch, name=name) for pattern, page, name in self.entries]

	def urlpatterns(self):
		return self.urlpatterns

	def menu_entries(self):
		return [(reverse(name), page.name) for pattern, page, name in self.entries]



class Menu:
	def __init__(self, site_map, template_name='basilica/menu.html',
				css_list_classes=list(), css_page_classes=list(), css_link_classes=list()):
		self.template = loader.get_template(template_name)
		self.site_map = site_map
		self.css_classes = {
			'list': css_list_classes,
			'page': css_page_classes,
			'link': css_link_classes
		}
	
	def render(self):
		return self.template.render({
			'entries': self.site_map.menu_entries,
			'css_classes': self.css_classes
		})

