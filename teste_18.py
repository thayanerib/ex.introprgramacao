def contador (a,b,c):
    x = a
    while x<=b:
        print(f'{x}', end='..')
        x+=c
    print('fim!')
contador(2,100,2)