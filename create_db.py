"""
Simple Time Tracker
A lightweight Python time tracker
Author C. Cardea
Created 02-10-2022
"""
from re import L
import sqlite3
DBFile = "/home/ccardea/repos/stt/__data__/stt.db"

create_tbl_records_sql = """
    CREATE TABLE IF NOT EXISTS records (
        projId INTEGER PRIMARY KEY,
        project TEXT,
        activity TEXT,
        start TEXT NOT NULL,
        stop TEXT NOT NULL,
        duration REAL,
        note TEXT
    );
"""

create_idx1_sql = """
    CREATE INDEX IF NOT EXISTS projIdx
        ON records (project);
"""

create_idx2_sql = """
    CREATE INDEX IF NOT EXISTS actIdx
        ON records (activity);
"""

create_idx3_sql = """
    CREATE INDEX IF NOT EXISTS startIdx
        ON records (start);
"""

if __name__ == "__main__":
    conn = sqlite3.connect(DBFile)
    cur = conn.cursor()
    cur.execute(create_tbl_records_sql)
    conn.commit()
    cur.execute(create_idx1_sql)
    cur.execute(create_idx2_sql)
    cur.execute(create_idx3_sql)
    conn.commit()
    conn.close()
