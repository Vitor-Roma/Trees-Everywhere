from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from trees.models import User, Tree, Location, Account, TreeData
from django.core.exceptions import ValidationError


class PlantedTreeTests(TestCase):
    fixtures = [
        'user_data.json',
        'account_data.json',
        'tree_data.json',
        'planted_tree_data.json',
    ]

    def setUp(self):
        self.user1 = get_object_or_404(User, pk=1)
        self.user2 = get_object_or_404(User, pk=1)

    def test_planted_tree_list_view(self):
        self.client.login(username="user1", password="password")
        response = self.client.get(reverse('user_planted_trees'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_planted_tree_detail_view_success(self):
        self.client.login(username="user1", password="password")
        response = self.client.get(reverse('detail_planted_tree', kwargs={"plant_tree_id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_planted_tree_detail_view_forbidden(self):
        self.client.login(username="user0", password="password")
        response = self.client.get(reverse('detail_planted_tree', kwargs={"plant_tree_id": 1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_plant_tree(self):
        tree_data = TreeData(
            tree=get_object_or_404(Tree, pk=1),
            location=Location(latitude=12.12345, longitude=12.12345)
        )
        planted_tree = self.user1.plant_tree(tree_data=tree_data)

        self.assertEqual(planted_tree.user, self.user1)

    def test_user_plant_trees(self):
        tree_list = [
            TreeData(
                tree=get_object_or_404(Tree, pk=1),
                location=Location(latitude=12.12345, longitude=12.12345)
            ),
            TreeData(
                tree=get_object_or_404(Tree, pk=1),
                location=Location(latitude=12.12345, longitude=12.12345)
            ),
            TreeData(
                tree=get_object_or_404(Tree, pk=1),
                location=Location(latitude=12.12345, longitude=12.12345)
            )
        ]
        planted_trees = self.user1.plant_trees(tree_list=tree_list)

        for planted_tree in planted_trees:
            self.assertEqual(planted_tree.user, self.user1)

    def test_get_all_user_accounts_tree(self):
        self.client.login(username="user2", password="password")
        self.client.get(reverse('accounts_dashboard'))
        response = self.client.get(reverse('accounts_dashboard'))

        self.assertTemplateUsed(response, 'account_dashboard.html')
        self.assertIn(f'<td>Pine</td>', response.content.decode('utf-8'))
        self.assertNotIn(f'<td>Maple</td>', response.content.decode('utf-8'))


    def test_plant_tree_invalid_account(self):
        with self.assertRaises(ValidationError):
            tree_data = TreeData(
                tree=get_object_or_404(Tree, pk=1),
                account=get_object_or_404(Account, pk=3),
                location=Location(
                    latitude=12.12345,
                    longitude=12.12345
                )
            )
            self.user1.plant_tree(tree_data)
