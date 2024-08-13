from django.contrib import admin
from trees.models import User, Account, PlantedTree, Tree, Profile
from django.contrib.auth.admin import UserAdmin


class AccountUser(admin.TabularInline):
    model = Account.users.through


class TreePlanted(admin.StackedInline):
    model = PlantedTree
    fk_name = 'tree'


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ('username', 'email', 'is_staff')
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('username', 'email', 'is_staff')

    inlines = [AccountUser]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name', 'active', 'users')
    filter_horizontal = ('users',)


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    inlines = [TreePlanted]


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):

    @staticmethod
    def tree_type(obj: PlantedTree) -> str:
        return obj.tree.scientific_name

    list_display = ('tree', 'tree_type')
    list_filter = ('tree__scientific_name', 'user__username')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('about', 'user')
    list_filter = ('about', 'user')
