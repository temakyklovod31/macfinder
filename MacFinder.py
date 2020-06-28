import requests

print('Выберете:\n1 Вычислить 1 MAC адрес\n2 Загрузить файл с Mac адресами')
a = input('Введите цифру действия:')

if a == '1':
    mac = input('Введите MAC адрес ')
    r = requests.get(f'https://api.mylnikov.org/geolocation/wifi?bssid={mac}')
    rg = r.json()
    lat = rg['data']['lat']
    lon = rg['data']['lon']
    print(lat, lon)
elif a == '2':
    wr = open('logs.txt', 'a')
    for mac in open('mac.txt'):
        mac = mac.replace('\n', '')
        r = requests.get(f'https://api.mylnikov.org/geolocation/wifi?bssid={mac}')
        rg = r.json()
        lat = rg['data']['lat']
        lon = rg['data']['lon']
        wr.write(f'{lat} {lon}\n')
    wr.close()
else:
    print('Вы ввели неверное значенние')