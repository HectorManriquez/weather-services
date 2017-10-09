from decimal import Decimal, getcontext


def to_farenheit(c):
    getcontext().prec = 3

    return (9 * c) / 5 + 32


def to_celsius(f):
    getcontext().prec = 3

    return (f - 32) * 5 / 9


def normalize_temps(f, c):
    getcontext().prec = 3

    return {
        'fahrenheit': Decimal(f) if f else to_farenheit(Decimal(c)),
        'celsius': Decimal(c) if c else to_celsius(Decimal(f))
    }
