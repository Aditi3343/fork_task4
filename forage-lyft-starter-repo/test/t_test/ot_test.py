import unittest
from tires.carriganTires import CarriganTires

class TestCT(unittest.TestCase):
    def test_needs_service_T(self):
        tire_wear = [0.7, 0.8, 0.9, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_F(self):
        tire_wear = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
