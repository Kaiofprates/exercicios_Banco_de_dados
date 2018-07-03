# coding: utf-8
import sqlite3

try:
    a = open('chords.db','r')
except IOError:
    a = open('chords.db','w')
    a.close()

conex = sqlite3.connect('chords.db')
cursor = conex.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS chords (note text, tabs text);')
nota = input('Acorde: ')
shape = open('acord.txt','r')
shape = shape.read()
n = """INSERT INTO chords (note,tabs) VALUES ("{}","{}");""".format(nota,shape)
lista = cursor.execute(n)
conex.commit()
conex.close()
