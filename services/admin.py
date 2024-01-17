from django.contrib import admin
from .models import Services2,Register1,Newmodel

class ServicesAdmin(admin.ModelAdmin):
    list_display=('id','heading','description','image')


class RegisterAdmin(admin.ModelAdmin):
    list_display =('address','email','birth','registerdate','registertime','phone')
class NewAdmin(admin.ModelAdmin):
    list_display =('email','name','phone')
admin.site.register(Services2,ServicesAdmin)
admin.site.register(Register1,RegisterAdmin)
admin.site.register(Newmodel,NewAdmin)

