class Connector:
    def __init__(self):
        self.__timeout = 60

connector = Connector()
# print(connector.__timeout) ### error
print(connector._Connector__timeout) ### name mangling