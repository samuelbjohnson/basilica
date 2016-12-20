from __future__ import unicode_literals

from django.db import models
from django.template import loader, Template
from misaka import Markdown, HtmlRenderer

markdown = Markdown(HtmlRenderer(), extensions=('fenced-code',))


# Create your models here.


class Content(models.Model):
	content_name = models.CharField('Content Name', max_length=256)
	is_draft = models.BooleanField('Draft')
	last_updated = models.DateTimeField('Last Updated', auto_now=True)
	
	content_value = ''
	template = loader.get_template('basilica/text.html')
	
	def get_content(self):
		return self.content_value

	def render(self):
		return self.template.render({
			'content': self.get_content()
		})
	
	class Meta:
		abstract = True


class Text(Content):
	content_value = models.CharField('Content Value', max_length=256)

	template = loader.get_template('basilica/text.html')


class Paragraph(Content):
	content_value = models.TextField('Content Value')

	template = loader.get_template('basilica/paragraph.html')


class MarkdownSection(Content):
	content_value = models.TextField('Content Value')
	template = loader.get_template('basilica/markdown.html')
	
	def get_content(self):
		return markdown(self.content_value)