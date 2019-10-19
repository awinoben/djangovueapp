from django.contrib import admin

# Register your models here.
from clients.models import Client

class ClientAdmin(admin.ModelAdmin):
  model = Client
  list_display = ('first_name', 'last_name', 'other_names' , 'dob', 'gender', 'occupation')

admin.site.register(Client,ClientAdmin)
