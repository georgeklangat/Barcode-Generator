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

# import barcode
# from barcode.writer import ImageWriter
# from PIL import Image

# # Function to generate barcode for a given product code
# def generate_barcode(product_code):
#     barcode_format = barcode.get_barcode_class('upc')
#     my_barcode = barcode_format(product_code, writer=ImageWriter())
#     filename = f"generated_barcode_{product_code}"
#     my_barcode.save(filename)
#     return filename + '.png'
#
# # Example product code
# product_code = '123456789012'
# barcode_image = generate_barcode(product_code)
#
# # Open and display the generated barcode image
# img = Image.open(barcode_image)
# img.show()
#
# # In a real POS system, you would scan the barcode and retrieve product details from the database

# PRACTICALS

# product_codes = [
#     '38197188541',
#     '34279573534',
#     '85959357320',
#     '34856475366',
# ]
#
# barcode_format = barcode.get_barcode_class('upc')
# for number in product_codes:
#     my_barcode = barcode_format(number, writer=ImageWriter())
#     filename = f"generated_barcode_{number}"
#     my_barcode.save(filename)
#
#     img = Image.open(f"{filename}.png")
#     img.show()
