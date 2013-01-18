from redactor.widgets import AdminRedactorEditor
from django.db import models

class RedactorAdmin():
	'''A baseclass for contrib.admin that renders all TextFields with the Redactor rich tech editor.
	This needs to be the first baseclass, before admin.ModelAdmin
	'''
	formfield_overrides = {
		models.TextField: {'widget': AdminRedactorEditor() }
	}