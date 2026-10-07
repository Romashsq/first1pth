FUEL_PRICE = float(input('Enter fuel price: ').strip())
CONSUMPTION_PER_100KM = float(input('Enter consumption of fuel per 100km: ').strip())    

def get_info():
    dist = float(input('Enter distance (km): ').strip())

    expenses = (dist * CONSUMPTION_PER_100KM) / 100
    total_cost = expenses * FUEL_PRICE
    
    full_tens = int(dist // 10)
    remaining_km = int(dist % 10)

    print(f'TOTAL COST - {total_cost}')
    print(f'FULL - {full_tens}')
    print(f'REMAINING KM!- {remaining_km}')
get_info()