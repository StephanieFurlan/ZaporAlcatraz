import sqlite3
import datetime

con = sqlite3.connect('BazaZapor.db')
# detect_types=sqlite3.PARSE_DECLTYPES
con.row_factory = sqlite3.Row

def v_slovarje(seznam):
    ''' Funkcija vrne seznam slovarjev '''
    return [dict(row) for row in seznam]

def je_prestopno(leto):
    '''Funkcija vrne True ali False glede na to ce je leto
       prestopno.'''
    if leto % 4 == 0:
        if leto % 100 == 0:
            if leto % 400 == 0:
                return True
            return False
        return True
    return False
                        
def koliko_dni(zapornik):
    datum = datum_aretiranja(zapornik)
    sql = '''
          SELECT sum(trajanje) AS dolzina
          FROM zlocin
          WHERE zlocinec = ? AND datum_prihoda = ?
          '''
    return con.execute(sql, [zapornik, datum]).fetchone()['dolzina']

def datum_aretiranja(zapornik):
    sql = '''
          SELECT MAX(datum_prihoda) AS zadnji
          FROM zlocin
          WHERE zlocinec = ?
          '''
    return con.execute(sql, [zapornik]).fetchone()['zadnji']
        
