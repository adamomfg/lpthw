# This is going to assign the int variable 100 to the name cars.
cars = 100
# This is going to assign to the variable space_in_a_car the float value 4.0.
space_in_a_car = 4.0
# This is going to assign the int value of 30 to the variable cars.
drivers = 30
# This is going to assign the int value of 90 to the variable passengers.
passengers = 90
# This line takes the value of the cars int, subtracts teh value of the
# drivers int, and assigns that value to the variable cars_not_driven.
cars_not_driven = cars - drivers
# This line assigns the value of the variable drivers to the variable
# cars_driven
cars_driven = drivers
# This line assigns the value of the multiplication of the values of the
# variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# this line assigns to the variable average_passengers_per_car to the division
# of the variable passengers by cars_driven
average_passengers_per_car = passengers / cars_driven

print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'to carpool today.'
print 'We need to put about', average_passengers_per_car, 'in each car.'
