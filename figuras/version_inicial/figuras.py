def area_circulo(radio):
    return 3.1416 * radio * radio


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


print("=== CÁLCULO DE ÁREAS DE FIGURAS GEOMÉTRICAS ===")

# Círculo
radio = 5
resultado_circulo = area_circulo(radio)

print("\nCÍRCULO")
print("Radio:", radio)
print("Área:", resultado_circulo)

# Rectángulo
base_rectangulo = 8
altura_rectangulo = 4
resultado_rectangulo = area_rectangulo(base_rectangulo, altura_rectangulo)

print("\nRECTÁNGULO")
print("Base:", base_rectangulo)
print("Altura:", altura_rectangulo)
print("Área:", resultado_rectangulo)

# Triángulo
base_triangulo = 10
altura_triangulo = 6
resultado_triangulo = area_triangulo(base_triangulo, altura_triangulo)

print("\nTRIÁNGULO")
print("Base:", base_triangulo)
print("Altura:", altura_triangulo)
print("Área:", resultado_triangulo)
