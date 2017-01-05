import sqlite3
import datetime

con = sqlite3.connect('BazaZapor.db')
# detect_types=sqlite3.PARSE_DECLTYPES
con.row_factory = sqlite3.Row

def v_slovarje(seznam):
    ''' Funkcija vrne seznam slovarjev '''
    return [dict(row) for row in seznam]

  
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

def kdaj_iz_zapora(zapornik):
    ''' Funkcija vrne datum, ko bo zapornik šel iz zapora'''
    slovar = {1: 31 , 2: 28, 3 : 31, 4:30, 5:31, 6:30,
            7:31, 8:31, 9: 30, 10: 31, 11:30, 12:31}
    
    stDni = koliko_dni(zapornik)
    datum = datum_aretiranja(zapornik).split('-')
    dan = int(datum[2])
    mesec = int(datum[1])
    leto = int(datum[0])
    # dodamo leta
    while stDni > 364:
        leto += 1
        stDni -= 365
    # dodamo mesece in dni
    treMesec = mesec
    treDan = dan
    while stDni != 0:
        vTemMesecu = slovar[treMesec]
        vTaMesec = vTemMesecu - treDan
        if vTaMesec <= stDni:
            # torej bomo skočili na naslendji mesec
            treDan = 0
            if treMesec == 12:
                treMesec = 1
                leto += 1
            else:
                treMesec += 1
            stDni -= vTaMesec 
        else:
            treDan += stDni
            stDni = 0
    if treDan <= 9:
        treDan = '0' + str(treDan)
    else:
        treDan = str(treDan)
    if treMesec <= 9:
        treMesec = '0' + str(treMesec)
    else:
        treMesec = str(treMesec)
    return print(leto,'-', treMesec, '-', treDan)
                
def poglej_zlocine(zapornik):
    '''funkcija vrne seznam zločin, ki jih je zapornik naredil'''
    sezZlocin = []
    sql = '''SELECT DISTINCT vrsta_zlocin AS vrsta
             FROM zlocin
             WHERE zlocinec = ?
          '''
    return v_slovarje(con.execute(sql, [zapornik]))

def kdo_je_v_celici(st_celice):
    ''' funkcija vrne id-je tistih, ki spijo z zapornikom'''
    sql = '''SELECT id      
             FROM osebe
             WHERE celica = ?        
            '''
    return v_slovarje(con.execute(sql, [st_celice]))

def proste_moske_celice():
    '''vrne seznam tistih celic, ki imajo se kako prosto mesto'''
    sql = ''' SELECT st_celice
              FROM celica
              WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  ) > 0
              AND tip LIKE 'M' '''
    return v_slovarje(con.execute(sql))
       
def proste_zenske_celice():
    '''vrne seznam tistih celic, ki imajo se kako prosto mesto'''
    sql = ''' SELECT st_celice
              FROM celica
              WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  ) > 0
              AND tip LIKE 'F' '''
    return v_slovarje(con.execute(sql))

def prosta_dela():
    SELECT delavec,
       kaj_dela,
       stevilo_ur,
       stevilo_ur * (
                        SELECT urna_postavka
                          FROM vrsta_dela
                         WHERE id = kaj_dela
                    )
       AS delano,
       (
           SELECT denarna_kazen
             FROM zlocin
            WHERE zlocinec = delavec
       )
       AS cena
  FROM delo
 WHERE cena > delano
 ORDER BY delavec;

SELECT kaj_dela,
       (
           SELECT stevilo_mest
             FROM vrsta_dela
            WHERE id = kaj_dela
       )
-      count(kaj_dela) 
  FROM delo
 GROUP BY kaj_dela;

