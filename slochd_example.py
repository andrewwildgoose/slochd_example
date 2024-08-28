# 1 mile = 1.609344 km
# 1 km = 0.621371192 miles

M_TO_KM_RATIO = 1.609344
KM_TO_M_RATIO = 0.621371192

# Will return slochd point in miles for miles total dist
SLOCHD_RATIO_3 = 0.6167619 # My calculation
SLOCHD_RATIO_4 = 0.61728395 # ChatGTP'S calculation

def calc_slochd(dist):
    '''
    Return the point at which the number of miles from the start is equal to the kilometers to the finish.
    INPUT:
        dist - float - total distance of the route in miles
    OUTPUT:
        slochd_point - float - point at which the number of miles from the start is equal to the kilometers to the finish
    '''
    slochd_point = dist * SLOCHD_RATIO_3

    return slochd_point

def miles_to_km(miles):
    '''
    Convert miles to kilometers
    INPUT:
        miles - float - distance in miles
    OUTPUT:
        kilometers - float - distance in kilometers
    '''
    kilometers = miles * M_TO_KM_RATIO
    return kilometers

def km_to_miles(kilometers):
    '''
    Convert kilometers to miles
    INOUT:
        kilometers - float - distance in kilometers
    OUTPUT:
        miles - float - distance in miles
    '''
    miles = kilometers * KM_TO_M_RATIO
    return miles

def main():
    dist1 = 100
    dist2 = 160
    dist3 = 80

    slochd1 = calc_slochd(dist1)
    slochd2 = calc_slochd(dist2)
    slochd3 = calc_slochd(dist3)

    miles_left_1 = dist1 - slochd1
    miles_left_2 = dist2 - slochd2
    miles_left_3 = dist3 - slochd3

    km_left_1 = miles_to_km(miles_left_1)
    km_left_2 = miles_to_km(miles_left_2)
    km_left_3 = miles_to_km(miles_left_3)

    print(f'Slochd point for {dist1} miles: {slochd1}')
    print(f'km left for {dist1} miles: {km_left_1}')

    print(f'Slochd point for {dist2} miles: {slochd2}')
    print(f'km left for {dist2} miles: {km_left_2}')

    print(f'Slochd point for {dist3} miles: {slochd3}')
    print(f'km left for {dist3} miles: {km_left_3}')

if __name__ == '__main__':
    main()
    
    
