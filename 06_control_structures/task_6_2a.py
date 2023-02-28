# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip-адрес: ")

n=0
ip_chek=True
for i in ip.split('.'):
   if not i.isdigit() or int(i)>255 or int(i)<0:
      ip_chek=False
      break
   n+=1
if ip_chek and n==4:
   octet = int(ip.split(".")[0])
   if octet >= 1 and octet <= 223:
      print("unicast")
   elif octet >= 224 and octet <= 239:
      print("multicast")
   elif ip == "255.255.255.255":
      print("local broadcast")
   elif ip == "0.0.0.0":
      print("unassigned")
   else:
      print("unused")
else:
   print('Неправильный IP-адрес')