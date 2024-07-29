import sqlite3

def get_column_names(table_name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    conn.close()
    column_names = [column[1] for column in columns]
    return column_names
def createNewTable(newName, columns):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    columns_sql = ", ".join(f"{col} TEXT" for col in columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {newName} ({columns_sql})")
    conn.commit()
    conn.close()

def combinedTable(newName, oldNames):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    for table_name in oldNames:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]

        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))

        cursor.execute(f"INSERT INTO {newName} ({columns_str}) SELECT {columns_str} FROM {table_name}")

    conn.commit()
    conn.close()

firstHand = ["eq_1_5h", "eq_1h", "eq_2h", "eq_wand"]
secondHand = ["eq_secondWeapon", "eq_orb", "eq_shield", "eq_arrow"]
firstHandAttribs = []
secondHandAttribs = []
for i in firstHand:
    firstHandAttribs+=get_column_names(i)
for j in secondHand:
    secondHandAttribs += get_column_names(j)
firstHandAttribs = set(firstHandAttribs)
print(firstHandAttribs)
secondHandAttribs = set(secondHandAttribs)
createNewTable("eq_firstHand", firstHandAttribs)
combinedTable("eq_firstHand", firstHand)
createNewTable("eq_secondHand", secondHandAttribs)
combinedTable("eq_secondHand", secondHand)
