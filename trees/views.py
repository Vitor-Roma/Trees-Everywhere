from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from trees.models import PlantedTree, Account, Tree, Location, TreeData
from django.core.exceptions import PermissionDenied


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        next = request.GET.get("next", "/")

        if user:
            auth.login(request, user)
            return redirect(next)
        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect(reverse('login'))
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))


@login_required
def home(request):
    return redirect(user_dashboard)


@login_required
def user_dashboard(request):
    user_accounts = Account.objects.filter(users=request.user, active=True)
    user_trees = PlantedTree.objects.filter(user=request.user)
    tree_list = Tree.objects.all()
    data = {
        "user_trees": user_trees,
        "user_accounts": user_accounts,
        "tree_list": tree_list,
    }
    return render(request, 'user_dashboard.html', data)


@login_required
def account_dashboard(request):
    user_accounts = request.user.account_users.filter(active=True)
    tree_list = Tree.objects.all()
    data = {
        "tree_list": tree_list,
        "user_accounts": user_accounts
    }
    return render(request, 'account_dashboard.html', data)


@login_required
def plant_new_tree(request):
    tree_data = TreeData(
        account=get_object_or_404(Account, pk=request.POST.get('account')),
        tree=get_object_or_404(Tree, pk=request.POST.get('tree')),
        location=Location(latitude=request.POST.get('latitude'), longitude=request.POST.get('longitude'))
    )
    request.user.plant_tree(tree_data)
    return redirect(home)


@login_required
def create_new_tree(request):
    name = request.POST.get('name')
    scientific_name = request.POST.get('scientific_name')
    Tree.objects.create(name=name, scientific_name=scientific_name)
    return redirect(home)


@login_required
def detail_plant_tree(request, plant_tree_id):
    planted_tree = get_object_or_404(PlantedTree, pk=plant_tree_id)

    if request.user != planted_tree.user:
        raise PermissionDenied("Você tem permissão acessar essa página!")
    return redirect(home)


@login_required
def delete_plant_tree(request, plant_tree_id):
    planted_tree = get_object_or_404(PlantedTree, pk=plant_tree_id)
    planted_tree.delete()

    return redirect(home)

