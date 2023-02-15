import insectclass as i

mosquito = i.insect('mosquito',2,4)
housefly = i.insect('housefly',2,4)

mosquito.flight_length()
housefly.flight_length()

print(f'the {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles',)
print(f'the {housefly.get_name()} can fly up to {housefly.get_miles()} miles',)

