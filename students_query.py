import sqlite3

def execute_query(sql: str, params: tuple = ()) -> list:
    try:
        with sqlite3.connect('students.db') as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(sql, params)
            return [dict(row) for row in cur.fetchall()]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

