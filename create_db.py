"""
Simple Time Tracker
A lightweight Python time tracker
Author C. Cardea
Created 02-10-2022
"""
import os.path
import sqlite3

dir = os.path.dirname(os.path.realpath(__file__))
DBFile = os.path.join(dir, "data/stt.db")

create_tbl_records_sql = """
    CREATE TABLE IF NOT EXISTS records (
        projId INTEGER PRIMARY KEY,
        project TEXT,
        activity TEXT,
        start TEXT NOT NULL,
        stop TEXT NOT NULL,
        duration REAL,
        comment TEXT
    );
"""

create_idx_sql = """
    CREATE INDEX IF NOT EXISTS projIdx
        ON records (project);

    CREATE INDEX IF NOT EXISTS actIdx
        ON records (activity);

    CREATE INDEX IF NOT EXISTS startIdx
        ON records (start);
"""
def create():
    conn = sqlite3.connect(DBFile)
    cur = conn.cursor()
    cur.execute(create_tbl_records_sql)
    conn.commit()
    cur.executescript(create_idx_sql)
    
    conn.commit()
    conn.close()
    return;

if __name__ == "__main__":
    create()    
