"""
    a script for pushing backups
    provided the database must not be running
    and it should restart the backup is pushed
"""

def stop_database():
    print("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")

class DBHandler:
    def __init__(self) -> None:
        self.db_name = "hello world"
    
    # this enter dunder must be present to use the instance
    def __enter__(self) ->"DBHandler":
        stop_database()
        return self

    # even if we have an error this will called
    # by default the arguments are none when their will be no erorr
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

def db_backup(db_name:str):
    print(f"backup database {db_name}")


with DBHandler() as db:
    db_backup(db.db_name)