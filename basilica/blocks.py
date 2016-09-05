from django.template import loader, TemplateDoesNotExist
from django.views.generic import View
from django.http import HttpResponse
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

	
	def get(self, request):
		return HttpResponse(self.loaded_template.render(self.context, request))
		
