from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

class FlatPageAdmin(FlatPageAdmin): # Define a new FlatPageAdmin
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),}),)

admin.site.unregister(FlatPage)  # Re-register FlatPageAdmin
admin.site.register(FlatPage, FlatPageAdmin)



