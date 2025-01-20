import barcode
from barcode.writer import ImageWriter
from PIL import Image

# List of product codes
product_codes = [
    '123456789012',
    '234567890123',
    '345678901234',
    # Add more product codes as needed
]

# Barcode format
barcode_format = barcode.get_barcode_class('upc')

# Loop through each product code and generate a barcode
for number in product_codes:
    my_barcode = barcode_format(number, writer=ImageWriter())
    filename = f"generated_barcode_{number}"
    my_barcode.save(filename)

    # Open and display the generated barcode image
    img = Image.open(f'{filename}.png')
    img.show()
