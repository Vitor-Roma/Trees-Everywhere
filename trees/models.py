from dataclasses import dataclass
from django.contrib.auth.models import AbstractUser
from django.db import models


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


@dataclass
class TreeList:
    tree: Tree
    location: Location


class PlantedTree(BaseModel):
    age = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey("User", on_delete=models.PROTECT, related_name="user_planted_tree")
    tree = models.ForeignKey("Tree", on_delete=models.CASCADE, related_name="tree_planted_tree")
    account = models.ForeignKey("Account", on_delete=models.PROTECT, null=True, blank=True, related_name="account_planted_tree")
    latitude = models.DecimalField(max_digits=20, decimal_places=5, null=False, blank=False)
    longitude = models.DecimalField(max_digits=20, decimal_places=5, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.tree} planted at : {self.location}"

    @property
    def location(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    def plant_tree(self, tree: Tree, location: Location) -> PlantedTree:
        planted_tree = PlantedTree.objects.create(
            tree=tree,
            user=self,
            age=0,
            latitude=location.latitude,
            longitude=location.longitude
        )

        return planted_tree

    def plant_trees(self, tree_list: list[TreeList]) -> list[PlantedTree]:
        tree_list_obj = [PlantedTree(
            tree=tree.tree,
            user=self,
            age=0,
            latitude=tree.location.latitude,
            longitude=tree.location.longitude
        ) for tree in tree_list]

        planted_trees = PlantedTree.objects.bulk_create(tree_list_obj)

        return planted_trees


class Account(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(null=True, blank=False, default=True)
    users = models.ManyToManyField("User", related_name="account_users")

    def __str__(self) -> str:
        return f"{self.name}"


class Profile(BaseModel):
    about = models.TextField(null=True, blank=True, default="")
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user_profile")

    def __str__(self) -> str:
        return f"{self.user} Profile"
