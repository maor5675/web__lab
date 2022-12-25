#extend for the Original User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info',{'fields' : ('first_name','last_name','email','age','City','Full_address','Postal_Code','Phonenumber','Role')})
UserAdmin.fieldsets = tuple(fields)
admin.site.register(User,UserAdmin)






#from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

#class UserProfileInline(admin.StackedInline):
    #model = Staffmember
    #can_delete = False

#class AccountsUserAdmin(AuthUserAdmin):
    #def add_view(self, *args, **kwargs):
        #self.inlines = []
        #return super(AccountsUserAdmin,self).add_view(*args,**kwargs) 

    #def change_view(self, *args, **kwargs):
        #self.inlines = [UserProfileInline]
        #return super(AccountsUserAdmin,self).change_view(*args,**kwargs) 


#admin.site.unregister(User)