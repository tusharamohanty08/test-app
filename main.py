def mult(main):
    def main(a, b):
        return a * b
    return main


@mult
def main(a, b):
    return a + b


print(main(10, 40))
