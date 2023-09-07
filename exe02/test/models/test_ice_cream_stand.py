import unittest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):

    def test_flavors_available(self):
        #setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", ["Flocos", "Menta", "Chocolate"])
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis: Flocos, Menta, Chocolate"
        #test
        sabores = ice_cream.flavors_available()
        #result
        self.assertEqual(expected_result, sabores)

    def test_flavors_not_available(self):
        #setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", [])
        expected_result = "Estamos sem estoque atualmente!"
        #test
        sabores = ice_cream.flavors_available()
        #result
        self.assertEqual(expected_result, sabores)

    def test_find_flavor(self):
        # setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", ["Flocos", "Menta", "Chocolate"])
        sabor_procurado = "Flocos"
        expected_result = "Temos no momento Flocos!"
        # test
        sabor = ice_cream.find_flavor(sabor_procurado)
        # result
        self.assertEqual(expected_result, sabor)

    def test_find_flavor_error(self):
        # setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", ["Flocos", "Menta", "Chocolate"])
        sabor_procurado = "Morango"
        expected_result = "Não temos no momento Morango!"
        # test
        sabor = ice_cream.find_flavor(sabor_procurado)
        # result
        self.assertEqual(expected_result, sabor)

    def test_add_flavor(self):
        # setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", ["Flocos", "Menta", "Chocolate"])
        sabor_add = "Morango"
        expected_result = f"{sabor_add} adicionado ao estoque!"
        # test
        sabor = ice_cream.add_flavor(sabor_add)
        # result
        self.assertEqual(expected_result, sabor)

    def test_add_same_flavor(self):
        # setup
        ice_cream = IceCreamStand("grupo5", "Doceteria", ["Flocos", "Menta", "Chocolate"])
        sabor_add = "Flocos"
        expected_result = "Sabor já disponivel!"
        # test
        sabor = ice_cream.add_flavor(sabor_add)
        # result
        self.assertEqual(expected_result, sabor)
