from typing import List, Dict


class Sizing:
    def __init__(self, value: float, sec: int, mnemo_state: int, sence_state: int):
        """
        :type value: float - result of sizing
        :type sec: int - sec int UTC of sizing
        :type mnemo_state: int - state of object railway infrastructure into sizing moment [-1,0,1]
        :type sence_state: int - if this infrastructure object need to save it state [0,1].
            If equal 0 then mnemo_state = -1, else mnemo_state = 0|1
        """
        self.value: float = value
        self.sec: int = sec
        self.mnemo_state: int = mnemo_state
        self.sence_state: int = sence_state

    def __str__(self)->str:
        return f"(value:{self.value}, sec:{self.sec}, mst:{self.mnemo_state}, sst:{self.sence_state})"

    def __repr__(self)->str:
        return f"(value:{self.value}, sec:{self.sec}, mst:{self.mnemo_state}, sst:{self.sence_state})"


class Source:
    def __init__(self, name: str = "NoMatter", data: Sizing = None):
        self.name: str = name
        self.sizing: List[Sizing] = []
        if data is not None:
            self.append_sizing(data)

    def append_sizing(self, data: Sizing) -> None:
        self.sizing.append(data)


class Object:
    def __init__(self, name: str):
        self.name: str = name
        self.sources: Dict[str, Source] = {}

    def add_sizing(self, source_name: str, data: Sizing) -> None:
        if source_name in self.sources:
            self.sources[source_name].append_sizing(data)
        else:
            self.sources[source_name] = Source(source_name, data)


class Pool:
    def __init__(self):
        self.objects: Dict[str, Object] = {}

    def add(self, data: Object) -> None:
         self.objects[data.name] = data

    def add_data(self, iname: str, source: str, value: float, sec: int, mnemo_state: int, sence_state: int )-> None:
        if iname in self.objects:
            self.objects[iname].add_sizing(source, Sizing(value, sec, mnemo_state, sence_state))
        else:
            tmp = Object(iname)
            tmp.add_sizing(source, Sizing(value, sec, mnemo_state, sence_state))
            self.add(tmp)

def open_db(path: object) -> object:
    print(path)

    return path
