class Polynomial:
    def __init__(self, coefficients):
        # Verificar que coefficients sea una lista de números
        if not all(isinstance(c, (int, float)) for c in coefficients):
            raise ValueError("All coefficients should be numbers")
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff:
                if power == 0:
                    terms.append(f"{coeff}")
                elif power == 1:
                    terms.append(f"{coeff}x" if coeff != 1 else "x")
                else:
                    terms.append(f"{coeff}x^{power}" if coeff != 1 else f"x^{power}")
        return " + ".join(terms[::-1]).replace(' + -', ' - ')

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        return Polynomial(result)

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] -= other.coefficients[i]
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for self_power, self_coeff in enumerate(self.coefficients):
            for other_power, other_coeff in enumerate(other.coefficients):
                result[self_power + other_power] += self_coeff * other_coeff
        return Polynomial(result)

# Ejemplo de uso
poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial([3, 4])

print("Poly1:", poly1)
print("Poly2:", poly2)

sum_poly = poly1 + poly2
print("Sum:", sum_poly)

diff_poly = poly1 - poly2
print("Difference:", diff_poly)

product_poly = poly1 * poly2
print("Product:", product_poly)
