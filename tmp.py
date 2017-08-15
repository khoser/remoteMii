#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import MySQLdb

def main():
    readSQL()
    p = subprocess.Popen("./tmp.sh done", shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read()
    print(out)
    result = out.split()
    print(result)
    return 0

def readSQL():
    # соединяемся с базой данных
    db = MySQLdb.connect(host="192.168.1.150", user="remotemii", passwd="123456", db="remotemii", charset='utf8')
    # формируем курсор
    cursor = db.cursor()

    # запрос к БД
    sql = """SELECT * FROM actions ORDER BY `rig` Desc"""
    # выполняем запрос
    cursor.execute(sql)

    # получаем результат выполнения запроса
    data =  cursor.fetchall()
    # перебираем записи
    for rec in data:
        # извлекаем данные из записей - в том же порядке, как и в SQL-запросе
        #rec
        # выводим информацию
        print(rec)

    # закрываем соединение с БД
    db.close()

if __name__ == '__main__':
    main()
