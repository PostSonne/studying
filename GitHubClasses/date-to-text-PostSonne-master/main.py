class DateToTextClass ():
  """
  Автор: Байрамова Алия, группа №P3355

  Решение реализовано внутри класса DateToTextClass и содержится внутри метода convert

  """
  date = input()
  time = input()
  def convert(date, time):
    day_list = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня','июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    date_list = date.split('.')

    year_decimal_list = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят','восемьдесят' ,'девяносто']

    year_ordinal_list = ['одиннадцатого', 'двенадцатого', 'тринадцатого', 'четырнадцатого','пятнадцатого', 'шестнадцатого', 'семнадцатого', 'восемнадцатого', 'девятнадцатого']

    year_ordinal_decimal_list = ['десятого', 'двадцатого','трицатого', 'сорокового', 'пятидесятого', 'шестидесятого', 'семидесятого', 'восьмидесятого','девяностого']

    year_numbers_list = ['первого' ,'второго', 'третьего', 'четвертого', 'пятого', 'шестого','седьмого', 'восьмого', 'девятого']
    day = day_list[int(date_list[0]) - 1]

    month =  month_list[int(date_list[1]) - 1]

    millenium_numbers = 'две тысячи' if date_list[2][:-2] == '20' else 'две тысячи сто' if date_list[2][:-2] == '21' else 'тысяча девятьсот'

    is_even = int(date_list[2][2:]) % 10 == 0

    final_numbers = year_numbers_list[int(date_list[2][3:]) - 1] if date_list[2][2:3] == "0" else year_ordinal_decimal_list[int(date_list[2][2:-1]) - 10] if is_even else year_ordinal_list[int(date_list[2][2:]) - 11] if int(date_list[2][2:]) < 20 else year_decimal_list[int(date_list[2][2:-1]) - 2] + ' ' + year_numbers_list[int(date_list[2][3:]) - 1]

    time_list = time.split(':')

    common_hours_numbers = ['пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре']

    common_time_numbers = ['пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре',' тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть','сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят']

    is_one_hour = int(time_list[0][0:2]) < 2

    is_one_minute = int(time_list[1][0:2]) < 2

    is_one_second = int(time_list[2][0:2]) < 2

    hours_under_five = ['один', 'два', 'три', 'четыре']

    minutes_under_five = ['одна', 'два', 'три', 'четыре']

    seconds_under_five = ['одна' ,'два', 'три', 'четыре']

    hours = hours_under_five[int(time_list[0][0:2]) -1] + ' час' if is_one_hour else hours_under_five[int(time_list[0][0:2])] + 'часа' if int(time_list[0][0:2]) < 6 else common_hours_numbers[int(time_list[0][0:2]) -5] + ' часов'

    minutes = minutes_under_five[int(time_list[1][0:2]) -1] + ' минута' if is_one_minute else minutes_under_five[int(time_list[1][0:2])] + ' минуты' if int(time_list[1][0:2]) < 6 else common_time_numbers[int(time_list[1][0:2]) -5] + ' минут'

    seconds = seconds_under_five[int(time_list[2][0:2]) -1] + ' секунда' if is_one_second else seconds_under_five[int(time_list[2][0:2]) -1] + ' секунды' if int(time_list[2][0:2]) < 6 else common_time_numbers[int(time_list[2][0:2]) -5] + ' секунд'

    return (day  + ' ' + month + ' ' + millenium_numbers + ' ' + final_numbers + ' года' + ' ' + hours + ' ' + minutes + ' ' + seconds)
  
  assert convert('25.09.2019', '08:17:59') == "двадцать пятое сентября две тысячи девятнадцатого года восемь часов семнадцать минут пятьдесят девять секунд", "Ошибка в тестовом примере 1"
  assert convert('01.01.2001', '01:01:01') == "первое января две тысячи первого года один час одна минута одна секунда", "Ошибка в тестовом примере 2"
  assert convert('06.12.1999', '06:20:60') == "шестое декабря тысяча девятьсот девяносто девятого года шесть часов двадцать минут шестьдесят секунд", "Ошибка в тестовом примере 3"
  assert convert('04.06.2013', '08:09:40') == "четвёртое июня две тысячи тринадцатого года восемь часов девять минут сорок секунд", "Ошибка в тестовом примере 4"
  assert convert('08.09.2003', '12:01:45') == "восьмое сентября две тысячи третьего года двенадцать часов одна минута сорок пять секунд", "Ошибка в тестовом примере 5"



