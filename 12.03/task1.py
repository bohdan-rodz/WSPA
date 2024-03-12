class Kalkulator:
    def dodawanie(self, x, y):
        return x + y

    def odejmowanie(self, x, y):
        return x - y

    def mnozenie(self, x, y):
        return x * y

    def dzielenie(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Nie można dzielić przez zero!"

object1 = Kalkulator()
object2 = Kalkulator()

print(object1.dodawanie(56, 88))
print(object2.dzielenie(23,11.5))