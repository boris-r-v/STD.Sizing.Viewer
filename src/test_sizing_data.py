import unittest

from sizing_data import Source, Sizing, Object, Pool


class TestSizing(unittest.TestCase):
    def setUp(self):
        self.sizing = Sizing(value=12.2, sec=123456789987, mnemo_state=0, sence_state=1)

class TestSizingInit(TestSizing):
    def test_init(self):
        self.assertEqual(self.sizing.value, 12.2)
        self.assertEqual(self.sizing.sec, 123456789987)
        self.assertEqual(self.sizing.mnemo_state, 0)
        self.assertEqual(self.sizing.sence_state, 1)

class TestSource(unittest.TestCase):
    def setUp(self) -> None:
        self.source = Source(u"first_1СП")
        self.source.append_sizing(Sizing(value=12.2, sec=123456789987, mnemo_state=0, sence_state=1))
        self.source.append_sizing(Sizing(value=0.5, sec=123, mnemo_state=20, sence_state=111))
        self.source2 = Source()

class TestSourceInit(TestSource):
    def test_init(self):
        self.assertEqual(self.source.name, u"first_1СП")
        self.assertEqual(self.source2.name, "NoMatter")

        self.assertEqual(self.source.sizing[0].value, 12.2)
        self.assertEqual(self.source.sizing[0].sec, 123456789987)
        self.assertEqual(self.source.sizing[0].mnemo_state, 0)
        self.assertEqual(self.source.sizing[0].sence_state, 1)

        self.assertEqual(self.source.sizing[1].value, 0.5)
        self.assertEqual(self.source.sizing[1].sec, 123)
        self.assertEqual(self.source.sizing[1].mnemo_state, 20)
        self.assertEqual(self.source.sizing[1].sence_state, 111)

class TestObject(unittest.TestCase):
    def setUp(self) -> None:
        self.object = Object(u"1/4СПГ")
        self.object.add_sizing(u"Постоянное", Sizing(value=12.2, sec=123456789987, mnemo_state=0, sence_state=1))
        self.object.add_sizing(u"Постоянное", Sizing(value=0.5, sec=123, mnemo_state=20, sence_state=111))

        self.object.add_sizing(u"Реле", Sizing(value=5.5, sec=321, mnemo_state=2, sence_state=15))
        self.object.add_sizing(u"Реле", Sizing(value=500.5, sec=12340321, mnemo_state=200, sence_state=5))
        self.object.add_sizing(u"Реле", Sizing(value=5.5, sec=321, mnemo_state=2, sence_state=15))

class TestObjectInit(TestObject):
    def test_init(self):
        self.assertEqual(self.object.name, u"1/4СПГ")
        self.assertEqual(self.object.sources[u"Постоянное"].name, u"Постоянное")
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[0].value, 12.2)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[0].sec, 123456789987)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[0].mnemo_state, 0)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[0].sence_state, 1)

        self.assertEqual(self.object.sources[u"Постоянное"].sizing[1].value, 0.5)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[1].sec, 123)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[1].mnemo_state, 20)
        self.assertEqual(self.object.sources[u"Постоянное"].sizing[1].sence_state, 111)

        self.assertEqual(self.object.sources[u"Реле"].name, u"Реле")
        self.assertEqual(self.object.sources[u"Реле"].sizing[0].value, 5.5)
        self.assertEqual(self.object.sources[u"Реле"].sizing[0].sec, 321)
        self.assertEqual(self.object.sources[u"Реле"].sizing[0].mnemo_state, 2)
        self.assertEqual(self.object.sources[u"Реле"].sizing[0].sence_state, 15)

        self.assertEqual(self.object.sources[u"Реле"].sizing[1].value, 500.5)
        self.assertEqual(self.object.sources[u"Реле"].sizing[1].sec, 12340321)
        self.assertEqual(self.object.sources[u"Реле"].sizing[1].mnemo_state, 200)
        self.assertEqual(self.object.sources[u"Реле"].sizing[1].sence_state, 5)
        
class TestPool(unittest.TestCase):
    def setUp(self) -> None:
        tmp = Object(u"1/4СПГ")
        tmp.add_sizing(u"Постоянное", Sizing(value=12.2, sec=123456789987, mnemo_state=0, sence_state=1))
        tmp.add_sizing(u"Постоянное", Sizing(value=0.5, sec=123, mnemo_state=20, sence_state=111))

        tmp.add_sizing(u"Реле", Sizing(value=5.5, sec=321, mnemo_state=2, sence_state=15))
        tmp.add_sizing(u"Реле", Sizing(value=500.5, sec=12340321, mnemo_state=200, sence_state=5))
        tmp.add_sizing(u"Реле", Sizing(value=5.5, sec=321, mnemo_state=2, sence_state=15))
        self.pool = Pool()
        self.pool.add(tmp)


class TestPoolInit(TestPool):
    def test_init(self):
        self.assertEqual( self.pool.objects[u"1/4СПГ"].name, u"1/4СПГ")
        self.assertEqual(self.pool.objects[u"1/4СПГ"].sources[u"Постоянное"].sizing[0].sec, 123456789987)

class TestPoolAddData(TestPool):
    def test_init(self):
        self.pool.add_data(u"1СП", u"Реле", 98.55, 12345, 111, 222)
        self.assertEqual(self.pool.objects[u"1СП"].name, u"1СП")
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[0].value, 98.55)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[0].sec, 12345)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[0].mnemo_state, 111)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[0].sence_state, 222)

        self.pool.add_data(u"1СП", u"Реле", 100.22, 12349, 222, 111)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[1].value, 100.22)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[1].sec, 12349)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[1].mnemo_state, 222)
        self.assertEqual(self.pool.objects[u"1СП"].sources[u"Реле"].sizing[1].sence_state, 111)

        self.pool.add_data(u"10СП", u"Реле", 98.55, 12345, 111, 222)
        self.assertEqual(self.pool.objects[u"10СП"].name, u"10СП")
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле"].sizing[0].value, 98.55)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле"].sizing[0].sec, 12345)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле"].sizing[0].mnemo_state, 111)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле"].sizing[0].sence_state, 222)

        self.pool.add_data(u"10СП", u"Реле2", 98.55, 12345, 111, 222)
        self.assertEqual(self.pool.objects[u"10СП"].name, u"10СП")
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле2"].sizing[0].value, 98.55)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле2"].sizing[0].sec, 12345)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле2"].sizing[0].mnemo_state, 111)
        self.assertEqual(self.pool.objects[u"10СП"].sources[u"Реле2"].sizing[0].sence_state, 222)

class TestPoolGetData(unittest.TestCase):
    def test_init(self):
        self.pool = Pool()
        self.pool.add_data(u"1СП", u"Реле", 98.55, 12345, 111, 222)
        self.pool.add_data(u"1СП", u"Реле", 100.22, 12349, 222, 111)
        self.pool.add_data(u"10СП", u"Реле", 98.55, 12345, 111, 222)
        self.pool.add_data(u"10СП", u"Реле2", 98.55, 12345, 111, 222)
        self.assertEqual(self.pool.get_objects_names(), [u"1СП", u"10СП"])
        self.assertEqual(self.pool.get_objects()[u"1СП"].name, u"1СП")
        self.assertEqual(self.pool.get_objects()[u"10СП"].name, u"10СП")

    def test_clear(self):
        self.pool = Pool()
        self.pool.add_data(u"1СП", u"Реле", 98.55, 12345, 111, 222)
        self.pool.add_data(u"1СП", u"Реле", 100.22, 12349, 222, 111)
        self.pool.add_data(u"10СП", u"Реле", 98.55, 12345, 111, 222)
        self.pool.add_data(u"10СП", u"Реле2", 98.55, 12345, 111, 222)
        self.assertEqual(self.pool.get_objects_names(), [u"1СП", u"10СП"])
        self.assertEqual(self.pool.get_objects()[u"1СП"].name, u"1СП")
        self.assertEqual(self.pool.get_objects()[u"10СП"].name, u"10СП")
        self.pool.clear()
        self.assertEqual(len(self.pool.get_objects_names()), 0 )
        self.assertEqual(len(self.pool.get_objects()), 0)
        self.assertEqual(len(self.pool.objects), 0)