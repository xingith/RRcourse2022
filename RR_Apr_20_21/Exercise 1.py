for i in range(100):
    fizz = int(i % 3 / 2) * "Fizz"
    buzz = int(i % 5 / 4) * "Buzz"
    print(fizz + buzz or -~i)