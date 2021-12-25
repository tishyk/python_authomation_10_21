from lesson_20.descriptor.column import Column


class User:
    id = Column("id", str)
    name = Column("name", str)
    age = Column("age", int)



if __name__ == "__main__":
    user = User()
    user.id = "1"
    user.name = "John"
    user.age = 23
    print(user.name)