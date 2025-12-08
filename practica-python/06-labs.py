#
# precio_base = [15.50, 45.00, 120.75, 9.99, 65.00]
# IMPUESTO = 0.15
# for p in precio_base:
#     precio_final = p + (p * IMPUESTO)
#     print(f"Base: {p}| Final (con 15% impuestos): {precio_final}")

precio_base = [12.60, 9.99, 120.50, 5.95]
impuesto = 0.15

for precio in precio_base:
    precio_final = precio * (1 + impuesto)
    print(f"Base| {precio}| Final (con 15% impuestos): {precio_final:.2f}")