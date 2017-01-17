# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from autofixture import AutoFixture
from ipm_system.core.models import Customer, Hardware


class TestAccessViews(TestCase):

    def tearDown(self):
        from django.db import connection
        connection.close()

    def setUp(self):
        self.client = Client()

    def test_access_home(self):

        resp = self.client.get(reverse('home'),)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Home", resp.content)

    def test_access_list_customer(self):

        resp = self.client.get(reverse('list_customer'),)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Clientes", resp.content)

    def test_access_edit_customer(self):
        resp = self.client.post(reverse('edit_customer', args=("add",)),
                                {'name': 'Test_customer', "submitted": "True"})
        self.assertEqual(resp.status_code, 302)

        find = Customer.objects.filter(name="Test_customer")
        self.assertEqual(find.count(), 1)

    def test_access_view_customer(self):
        customer = AutoFixture(Customer).create(1)[0]

        resp = self.client.get(reverse('view_customer', args=(customer.id,)),)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(customer.name, resp.content)

    def test_access_edit_hardware(self):
        customer = AutoFixture(Customer).create(1)[0]

        resp = self.client.post(
            reverse('edit_hardware', args=(customer.id, "add")),
            {'name': 'Test_hardware', "submitted": "True"})
        self.assertEqual(resp.status_code, 302)

        find = Hardware.objects.filter(name="Test_hardware")
        self.assertEqual(find.count(), 1)

    def test_access_download_license(self):
        customer = AutoFixture(Customer).create(1)[0]
        hardware = AutoFixture(Hardware, field_values={
            "customer": customer
        }).create(1)[0]

        resp = self.client.get(
            reverse('download_license', args=(customer.id, hardware.id))
        )
        self.assertEqual(resp.status_code, 200)
