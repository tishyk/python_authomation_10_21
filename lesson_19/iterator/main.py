from lesson_20.iterator.car import Car
from lesson_20.iterator.taxi_park import TaxiPark


if __name__ == "__main__":
    toyota = Car("Toyota", "Yellow", "12345")
    mitsubishi = Car("Mitsubishi", "Red", "32154")
    mercedes = Car("Mercedes", "Green", "12567")
    tesla = Car("Tesla", "Brown", "12678")
    hunday = Car("Hunday", "Yellow", "12789")

    taxi_park = TaxiPark([toyota, mitsubishi, mercedes, tesla, hunday])
    # taxi_park.add_cars([toyota, mitsubishi, mercedes, tesla, hunday])
    
    for car in taxi_park:
        print(car)
