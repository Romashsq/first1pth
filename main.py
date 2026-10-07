quantity_in_saved = [
    {'id': 1, 'product_name': 'Laptop1', 'price': 100},
    {'id': 2, 'product_name': 'Laptop2', 'price': 2321},
    {'id': 3, 'product_name': 'Laptop3', 'price': 3330},
]

delivery_cost = 200

def get_total(products):
        bucket = sum(product['price'] for product in products)
        total = bucket + delivery_cost
        for product in products: 
                print(f'ID: {product['id']}, NAME: {product['product_name']}, PRICE: {product['price']},')
        print(f'Total price is {total}')
    
get_total(quantity_in_saved)

