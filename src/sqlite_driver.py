import sqlite3
import sizing_data


class SqliteDriver:
    def __init__(self, path: str):
        self.path: str = path

    def select_data(self) -> sizing_data.Pool:
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        pool = sizing_data.Pool()
        for (iname, source, value, limit_state_dummy, mnemo_state, sence_state, sec) in cursor.execute("SELECT iname, source, value, limit_state, mnemo_state, sence_state, sec FROM all_sizing ORDER BY iname, source"):
            pool.add_data(iname=iname, source=source, value=value, sec=sec, mnemo_state=mnemo_state, sence_state=sence_state)
        conn.close()
        return pool

def get_pool( path: str)->sizing_data.Pool:
    drv = SqliteDriver(path=path)
    return drv.select_data()
