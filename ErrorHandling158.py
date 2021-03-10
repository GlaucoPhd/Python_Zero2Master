while True:
    try:
        age = int(input('Age: '))
        10 / age
        raise ValueError('Cut Out.')
    except ZeroDivisionError:
        print('Grater than 0')
        break
    else:
        print('Thanks')
    finally:
        print('Done')
    print('I am here')
