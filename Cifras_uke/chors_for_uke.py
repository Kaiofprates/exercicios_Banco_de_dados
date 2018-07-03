# coding: utf-8
import sqlite3
conex = sqlite3.connect('chords.db')
cursor = conex.cursor()
note = input('Acorde? ')
lista = cursor.execute('select tabs from chords where note = "{}"'.format(note))
acorde = list(lista.fetchall())
acorde = str(acorde)

def trata_acorde(tabs):
    tabs = tabs.replace('[','').replace(']','').replace('(','').replace(')','').replace(',','').replace(r'\n','\n')
    return print(tabs)

acorde = trata_acorde(acorde)
