from django import template

register = template.Library()

@register.assignment_tag
def changetherating(self, rate):
	self.rated_capacity = rate
	self.save()