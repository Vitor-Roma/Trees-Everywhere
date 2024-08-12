from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from trees.api.serializers import PlantedTreeSerializer
from trees.models import PlantedTree
from django.core.exceptions import PermissionDenied


class PlantedTreesViewSet(ListAPIView):
    serializer_class = PlantedTreeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        planted_tree_list = PlantedTree.objects.filter(user=self.request.user)
        return planted_tree_list


class PlantedTreesDetailViewSet(RetrieveAPIView):
    serializer_class = PlantedTreeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        planted_tree = get_object_or_404(PlantedTree, pk=kwargs.get('plant_tree_id'))
        if request.user != planted_tree.user:
            raise PermissionDenied("Você tem permissão acessar essa página!")
        return Response(self.get_serializer(planted_tree).data)
