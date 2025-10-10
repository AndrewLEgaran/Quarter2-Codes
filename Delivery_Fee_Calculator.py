Dist = int(input("Enter the distance in kilometers: "))
rpkm = int(input("Enter the rate per kilometer (Php): "))

def calculate_delivery_fee():
    return globals()['Dist'] * globals()['rpkm']


print("Total Delivery Fee: Php", calculate_delivery_fee())
