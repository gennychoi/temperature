fahrenheit = 0
print('Fahrenheit Celsius')
while fahrenheit <= 250:
    celcius = (fahrenheit - 32) / 1.8
    print('{:3d}{:14.2f}'.format(fahrenheit, celcius))
    fahrenheit = fahrenheit + 25