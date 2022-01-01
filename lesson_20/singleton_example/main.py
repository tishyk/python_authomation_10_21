from lesson_21.singleton_example.db.db import DbConnection


if __name__ == "__main__":
    connection_1 = DbConnection("localhost", 12325)
    connection_2 = DbConnection("192.168.0.1", 32154)
    print(connection_1)
    print(connection_2)