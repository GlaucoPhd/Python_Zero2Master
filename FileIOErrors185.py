try:
    with open('Texto.txt', mode='r') as meu_arquivo:
        print(meu_arquivo.read())
except FileNotFoundError as err:
    print('File does no exist.')
    raise err
except IOError as err:
    print('IO error')
    raise err