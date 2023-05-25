"""
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как
<имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок.
Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz,
третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков. В следующих
n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое
неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из последующих
m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались.
"""


def corporate_email():
    existing_emails = [input() for i in range(int(input()))]
    new_employees = [input() for i in range(int(input()))]
    for employee in new_employees:
        email = f'{employee}@beegeek.bzz'
        if email not in existing_emails:
            print(email)
            existing_emails.append(email)
        else:
            counter = 1
            while True:
                email = f'{employee}{counter}@beegeek.bzz'
                if email in existing_emails:
                    counter += 1
                    continue
                else:
                    print(email)
                    existing_emails.append(email)
                    break


corporate_email()

# Sample Input2:
# 2
# timyr-guev2@beegeek.bzz
# anri-tabuev@beegeek.bzz
# 3
# timyr-guev
# timyr-guev
# anri-tabuev
# Sample Output:
# timyr-guev@beegeek.bzz
# timyr-guev1@beegeek.bzz
# anri-tabuev1@beegeek.bzz
