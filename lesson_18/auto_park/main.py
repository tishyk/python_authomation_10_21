from lesson_18.auto_park.auto_park import AutoPark
from lesson_18.auto_park.car import Car


if __name__ == "__main__":
    auto_part = AutoPark()
    audi = Car(1968, "Yellow", "Audi")
    toyota = Car(1999, "Grey", "Toyota")
    mitzubishi = Car(2022, "Green", "Mitsubishi")
    mercedees = Car(2010, "Yellow", "Mercedes")

    auto_part[1111] = audi
    auto_part[2222] = mercedees
    auto_part[3333] = mitzubishi
    auto_part[4444] = toyota


    print(auto_part[1111])
    print(auto_part[2222])
    print(auto_part[3333])
    print(auto_part[4444])
