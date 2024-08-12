from django.contrib import admin
from django.urls import path
from trees.views import login, logout, user_dashboard, account_dashboard, home, plant_new_tree, create_new_tree, delete_plant_tree, detail_plant_tree
from rest_framework_simplejwt.views import TokenObtainPairView
from trees.api.viewsets import PlantedTreesViewSet, PlantedTreesDetailViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', logout, name='logout'),

    path('api/me/planted_trees/', PlantedTreesViewSet.as_view(), name='user_planted_trees'),
    path('api/me/planted_trees/<int:plant_tree_id>/', PlantedTreesDetailViewSet.as_view(), name='detail_planted_tree'),

    path('', home, name='home'),
    path('me/dashboard/', user_dashboard, name='user_dashboard'),
    path('accounts/dashboard/', account_dashboard, name='accounts_dashboard'),
    path('me/plant_new_tree', plant_new_tree, name='plant_new_tree'),
    path('me/create_new_tree', create_new_tree, name='create_new_tree'),
    path('me/delete_plant_tree/<int:plant_tree_id>/', delete_plant_tree, name='delete_plant_tree'),
]
