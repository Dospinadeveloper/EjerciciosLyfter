product_price = 0
discount = 0
final_price = 0

product_price = float(input("Digite el precio del producto " ) )

if product_price < 100:
    discount = product_price * 0.02
    final_price = product_price - discount
else:
    discount = product_price * 0.10
    final_price = product_price - discount
print (f"El precio final para este producto es de: {final_price:.2f}")