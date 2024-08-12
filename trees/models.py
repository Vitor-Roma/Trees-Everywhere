import datetime
from dataclasses import dataclass
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


@dataclass
class Location:
    longitude: float
    latitude: float


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tree(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    scientific_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name} - {self.scientific_name}"


class PlantedTree(BaseModel):
    user = models.ForeignKey("User", on_delete=models.PROTECT, related_name="user_planted_tree")
    tree = models.ForeignKey("Tree", on_delete=models.CASCADE, related_name="tree_planted_tree")
    account = models.ForeignKey("Account", on_delete=models.PROTECT, null=True, blank=True, related_name="account_planted_tree")
    latitude = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=False)
    longitude = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.tree} planted at : {self.location}"

    def clean(self):
        account = self.account if self.account else None
        if account and self.user not in account.users.all():
            raise ValidationError("O usuário não está associado a esta conta.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def location(self) -> str:
        return f"{self.latitude}, {self.longitude}"

    @property
    def age(self) -> str:
        return f"{self.tree.created_at.year - datetime.datetime.now().year} anos"


class Account(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(null=True, blank=False, default=True)
    users = models.ManyToManyField("User", related_name="account_users")

    def __str__(self) -> str:
        return f"{self.name}"


@dataclass
class TreeData:
    tree: Tree
    location: Location
    account: Account = None


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    def plant_tree(self, tree_data: TreeData) -> PlantedTree:
        planted_tree = PlantedTree.objects.create(
            tree=tree_data.tree,
            user=self,
            account=tree_data.account,
            latitude=tree_data.location.latitude,
            longitude=tree_data.location.longitude
        )

        return planted_tree

    def plant_trees(self, tree_list: list[TreeData]) -> list[PlantedTree]:
        tree_list_obj = [PlantedTree(
            tree=tree_data.tree,
            user=self,
            account=tree_data.account,
            latitude=tree_data.location.latitude,
            longitude=tree_data.location.longitude
        ) for tree_data in tree_list]

        planted_trees = PlantedTree.objects.bulk_create(tree_list_obj)

        return planted_trees

class Profile(BaseModel):
    about = models.TextField(null=True, blank=True, default="")
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user_profile")

    def __str__(self) -> str:
        return f"{self.user} Profile"
