from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("유저 정보", {"fields":("email", "nickname", "is_business", "password")}),
        ("Permission", {"fields":("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide', ),
            'fields':('email', 'nickname', 'is_business', 'password1', 'password2', ),
        }),
    )

    list_display =('email', 'nickname', 'is_business','is_active', 'is_staff')
    search_fields = ('email', 'nickname')
    ordering = ('email', )