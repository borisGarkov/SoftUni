import re

products_number = int(input())

for _ in range(products_number):
    barcode = input()
    pattern = r"^@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@[#]+"
    valid_barcode = re.findall(pattern, barcode)

    product_number = ""
    if len(valid_barcode) > 0:
        pattern_digit = r"\d"
        find_digits = re.findall(pattern_digit, barcode)
        for digit in find_digits:
            product_number += digit

        if len(product_number) == 0:
            product_number = "00"

        print(f"Product group: {product_number}")
        continue
    print("Invalid barcode")