from rest_framework import serializers
from trees.models import PlantedTree, Tree


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = '__all__'


class PlantedTreeSerializer(serializers.ModelSerializer):
    tree = TreeSerializer(many=False, read_only=True)

    class Meta:
        model = PlantedTree
        fields = ('id', 'age', 'created_at', 'tree', 'location')
