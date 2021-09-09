import unittest
from sqlite_driver import SqliteDriver, get_pool
from sizing_data import Source, Sizing, Object, Pool
import os


class TestSqliteDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.drv = SqliteDriver("../tests/test.db")

    def test_init(self):
        self.assertEqual(True, True)  # add assertion here

    def test_class_connect(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        self.pool: Pool = self.drv.select_data()
        self.assertNotEqual(len(self.pool.objects), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы A"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы B"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы C"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_2"].sources[u"Напряжение фазы B"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_2"].sources[u"Напряжение фазы C"].sizing), 0)

        self.assertNotEqual(len(self.pool.objects[u"svg2988@g6564"].sources[u"Данные"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"svg2988@g7462"].sources[u"Данные"].sizing), 0)

    def test_method_connect(self):
        self.pool: Pool = get_pool("../tests/test.db")
        self.assertNotEqual(len(self.pool.objects), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы A"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы B"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_1"].sources[u"Напряжение фазы C"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_2"].sources[u"Напряжение фазы B"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"Фидер_2"].sources[u"Напряжение фазы C"].sizing), 0)

        self.assertNotEqual(len(self.pool.objects[u"svg2988@g6564"].sources[u"Данные"].sizing), 0)
        self.assertNotEqual(len(self.pool.objects[u"svg2988@g7462"].sources[u"Данные"].sizing), 0)
