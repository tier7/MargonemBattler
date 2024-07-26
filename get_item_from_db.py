import sqlite3

def getItem(item_id,type):
    conn = sqlite3.connect('items.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM eq_{type} WHERE id=?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {key: row[key] for key in row.keys()}
    else:
        return None