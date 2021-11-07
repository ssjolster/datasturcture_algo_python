def leap(year):
    if year % 400 == 0:
        print('its a leap year')
    elif year % 100 == 0:
        print('its not a leap year')
    elif year % 4 == 0:
        print('its leap year')

    return leap


leap(2000)
