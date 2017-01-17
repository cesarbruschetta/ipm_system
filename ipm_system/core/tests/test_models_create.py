# -*- coding: utf-8 -*-
from django.test import TestCase

from autofixture import AutoFixture

from ipm_system.core.models import (Customer, Hardware, License)


class TestModelsCreate(TestCase):

    def test_create_customer(self):

        # Criando Customer
        customers = AutoFixture(Customer).create(3)

        # Vendo quantas criou
        count_customer = Customer.objects.count()
        self.assertTrue(count_customer == 3)

        # Vefificando os dados salvos
        check_customer = customers[0]
        obj_check = Customer.objects.get(id=check_customer.id)
        self.assertTrue(obj_check.name == check_customer.name)

    def test_create_hardware(self):

        # Criando Hardware
        hardwares = AutoFixture(Hardware, generate_fk=True).create(3)

        # Vendo quantas criou
        count_hardware = Hardware.objects.count()
        self.assertTrue(count_hardware == 3)

        # Vefificando os dados salvos
        check_hardware = hardwares[0]
        obj_check = Hardware.objects.get(id=check_hardware.id)
        self.assertTrue(obj_check.name == check_hardware.name)

    def test_create_license(self):

        # Criando License
        licenses = AutoFixture(License, generate_fk=True).create(3)

        # Vendo quantas criou
        count_license = License.objects.count()
        self.assertTrue(count_license == 3)

        # Vefificando os dados salvos
        check_license = licenses[0]
        obj_check = License.objects.get(id=check_license.id)
        self.assertTrue(obj_check.license == check_license.license)
