from django.contrib import admin
from CareHealthapp.models import *

# Register your models here.
admin.site.register(patient)
admin.site.register(Ward)
admin.site.register(Doctor)
admin.site.register(Appoint)
admin.site.register(Contact)


