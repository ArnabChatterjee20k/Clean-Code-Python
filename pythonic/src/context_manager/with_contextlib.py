import contextlib


def stop_database():
    print("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")


@contextlib.contextmanager
def db_handler():
    db_name = "db"
    try:
        stop_database()
        yield db_name
    finally:
        start_database()

def db_backup(db_name:str):
    print(f"backup database {db_name}")

with db_handler() as db:
    db_backup(db_name=db)


# use this if we wanna go with decorative approach and not with based
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self
    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup(db):
    db_backup(db)
    # raise Exception("erorr")

offline_backup("another db")