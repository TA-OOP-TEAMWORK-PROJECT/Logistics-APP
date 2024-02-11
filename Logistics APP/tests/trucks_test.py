import unittest
from models.actros import Actros
from models.man import Man
from models.scania import Scania
from models.truck_status import TruckStatus


class Trucks_Should(unittest.TestCase):


    def setUp(self):
        self.man = Man()
        self.scania = Scania()
        self.actros = Actros()

    def test_trucks_IfBrandIsCorrect(self):
        # Arrange & Act & Assert
        self.assertEqual(self.man.truck_brand, "Man")
        self.assertEqual(self.scania.truck_brand, "Scania")
        self.assertEqual(self.actros.truck_brand, "Actros")

    def test_trucks_IfMaxRangeIsCorrect(self):
        # Arrange & Act & Assert
        self.assertEqual(self.man.max_range_km, 10000)
        self.assertEqual(self.scania.max_range_km, 8000)
        self.assertEqual(self.actros.max_range_km, 13000)

    def test_truck_IfUpdatesTheLoadCorrectly(self):
        # Arrange
        truck = Man()
        initial_capacity = truck.capacity_kg

        # Act
        load_weight = initial_capacity // 2
        truck.update_load(load_weight)

        # Assert
        self.assertEqual(truck.current_load_kg, load_weight)
        # self.assertEqual(truck.status, TruckStatus.FREE)
        self.assertEqual(truck.status, TruckStatus.ON_THE_ROAD_NOT_FULL)
        self.assertNotEqual(truck.status, TruckStatus.ON_THE_ROAD_FULL)
        self.assertNotEqual(truck.status, TruckStatus.FREE)

    def test_truck_IfExceedsFullCapacity(self):
        # Arrange
        truck = Man()
        initial_capacity = truck.capacity_kg

        # Act
        load_weight = initial_capacity // 2
        truck.update_load(load_weight)

        # Assert
        with self.assertRaises(ValueError):
            truck.update_load(initial_capacity)

    def test_assign_route_IfTheTruckIsFree(self):
        # Arrange
        truck = Scania()

        # Act
        truck.assign_to_route("Route 22")

        # Assert
        self.assertEqual(truck.current_route, "Route 22")
        self.assertEqual(truck.status, TruckStatus.ON_THE_ROAD_NOT_FULL)

    def test_assign_route_IfTheTruckIsNotFree(self):
        # Arrange
        truck = Actros()
        truck.status = TruckStatus.ON_THE_ROAD_FULL

        # Act & Assert
        with self.assertRaises(Exception):
            truck.assign_to_route("Route 23")

    def test_release_truck(self):
        # Arrange
        truck = Man()

        # Act
        truck.assign_to_route("Route 22")
        truck.release()

        # Assert
        self.assertEqual(truck.status, TruckStatus.FREE)
        self.assertIsNone(truck.current_route)
        self.assertEqual(truck.current_load_kg, 0)
        self.assertTrue(truck.check_availability())

    def test_AssignAndReleaseRoute(self):
        # Arrange
        truck = Scania()

        # Act & Assert
        truck.assign_to_route("Route 22")
        self.assertNotEqual(truck.status, TruckStatus.FREE)

        # Act & Assert
        truck.release()
        self.assertEqual(truck.status, TruckStatus.FREE)



class TruckIdGenerator_Should(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     Scania.scania_id_generator.reset()
    #     Man.man_id_generator.reset()
    #     Actros.actros_id_generator.reset()

    def setUp(self):
        Scania.scania_id_generator.reset()
        Man.man_id_generator.reset()
        Actros.actros_id_generator.reset()
        self.scania_valid_id = {Scania().truck_id for _ in range(10)}
        self.man_valid_id = {Man().truck_id for _ in range(15)}
        self.actros_valid_id = {Actros().truck_id for _ in range(15)}

    def test_trucks_IfIDsAreWithinPredefinedRange(self):
        # Arrange & Act & Assert
        self.assertTrue(all(1001 <= ids <= 1010 for ids in self.scania_valid_id))
        self.assertTrue(all(1011 <= ids <= 1025 for ids in self.man_valid_id))
        self.assertTrue(all(1026 <= ids <= 1040 for ids in self.actros_valid_id))

    def test_id_IsUniqueAcrossAllTrucks(self):
        # Arrange
        all_ids = self.man_valid_id.union(self.scania_valid_id).union(self.actros_valid_id)
        print(f'This is what we print: {all_ids}')
        # Act
        expected_num_ids = len(self.man_valid_id) + len(self.scania_valid_id) + len(self.actros_valid_id)
        print(expected_num_ids)
        # Assert
        self.assertEqual(len(all_ids), expected_num_ids)

