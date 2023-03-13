import phonenumbers
from phonenumbers import timezone, geocoder, carrier

num = input("Enter number with +__: ")
phn = phonenumbers.parse(num)
timezone = timezone.time_zones_for_number(phn)
carrier = carrier.name_for_number(phn, 'en')
region = geocoder.description_for_number(phn, 'en')

print('''
-------------------------------------------------''')
print(phn)
print(timezone)
print(carrier)
print(region)
print("-------------------------------------------------")