from django.contrib import admin
from .models import Employe


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'email', 'salaire')
    search_fields = ('nom', 'poste', 'email')
    list_filter = ('poste',)
