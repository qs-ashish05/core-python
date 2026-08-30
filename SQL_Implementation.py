import os

class SQL_Implementation:
    def __init__(self):
        pass

    def createDatabase(self, tableName):
        command = f"mkdir {tableName}"
        os.system(command)
        print(f"{tableName} Database created")