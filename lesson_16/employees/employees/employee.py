class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str, 
        inn: int, 
        age: int,
        experience: int,
        rate: int
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._inn = inn
        self._age = age
        self._experience = experience
        self._rate  = rate
        self._got_premiya = False

    def do_work(self):
        print("I am working...")

    def get_premiya(self):
        return self._rate * self._experience
