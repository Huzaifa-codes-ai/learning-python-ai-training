car_stock = {
    "Brand": "Toyota",
    "Model": "Corolla",
    "Year": 2024
}

print("--- Keys ---")
for key in car_stock.keys():
    print(key)

print("\n--- Values ---")
for val in car_stock.values():
    print(val)

print("\n--- Items ---")
for k, v in car_stock.items():
    print(k + " is set to: " + str(v))
