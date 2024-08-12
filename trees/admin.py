from django.contrib import admin
from trees.models import User, Account, PlantedTree, Tree
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ('username', 'email')
    list_display = ('username', 'email')
    list_filter = ('username', 'email')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('name', 'active')


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):

    @staticmethod
    def tree_type(obj: PlantedTree) -> str:
        return obj.tree.scientific_name

    list_display = ('tree', 'tree_type')
    list_filter = ('tree__scientific_name', 'user__username')

