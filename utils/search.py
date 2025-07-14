def load_machines(self):
        conn = sqlite2.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS machines (
            machine_name TEXT, task TEXT, status TEXT, date TEXT
        )""")
        c.execute("SELECT * FROM machines")
        records = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()
         
def load_machines(self):
        conn = sqlite2.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS machines (
            machine_name TEXT, task TEXT, status TEXT, date TEXT
        )""")
        c.execute("SELECT * FROM machines")
        records = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()