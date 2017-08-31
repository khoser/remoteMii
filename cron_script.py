#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import MySQLdb
from socket import gethostname

hostname = gethostname()


def main():
    readSQL()
    return 0

def readSQL():
    # соединяемся с базой данных
    db = MySQLdb.connect(host="192.168.1.150", user="remotemii", passwd="123456", db="remotemii", charset='utf8')
    # формируем курсор
    cursor = db.cursor()

    # запрос к БД
    sql = "SELECT action FROM actions where rig = %s order by id"
    # выполняем запрос
    cursor.execute(sql, (hostname,))
    # получаем результат выполнения запроса
    data =  cursor.fetchall()
    # перебираем записи
    for rec in data:
        # извлекаем данные из записей - в том же порядке, как и в SQL-запросе
        action, = rec
        # выводим информацию
        #print("Выполняю:", action)
        p = subprocess.Popen("./run_sh.sh '"+action+"'", shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read()
        #print(out)
        #result = out.split()
        #print(result)
    # запрос к БД
    sql2 = "DELETE FROM actions where rig = %s"
    #print("Удаляю выполненные задачи")
    # выполняем запрос
    cursor.execute(sql2, (hostname,))
    # применяем изменения
    db.commit()
    # закрываем соединение с БД
    db.close()

if __name__ == '__main__':
    main()
