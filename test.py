test = {
    "0":"MIT",
    "1":"somethingelse"
}

try:
    print(test["2"])
except KeyError:
    print("KeyError")