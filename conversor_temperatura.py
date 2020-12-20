
def toFarenheit (celsius):
    farenheit = 9 / 5 * celsius + 32
    return farenheit


def toCelsius(farenheit):
    celsius = (farenheit - 32) / (9 / 5)
    return celsius

print(toFarenheit(100))
print(toCelsius(212))