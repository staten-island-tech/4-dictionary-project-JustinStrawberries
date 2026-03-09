def Tarifa(megabits, number_months, usage):
    value = 0
    for use in usage:
        value += megabits
        value -= use
    print(value + megabits)
Tarifa(10, 3, [4,6,2])