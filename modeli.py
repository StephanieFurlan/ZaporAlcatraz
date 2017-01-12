import sqlite3
import datetime
con = sqlite3.connect('BazaZapor.db')


def ime(id_st):
    '''funckija vrne ime zapornika z id_st-jem id'''
    sql = '''SELECT ime
            FROM osebe
            WHERE id = ?'''
    for ime in con.execute(sql,[id_st]):
        return ime[0]

def priimek(id_st):
    '''funckija vrne priimek zapornika z id-jem id'''
    sql = '''SELECT priimek
            FROM osebe
            WHERE id = ?'''
    for priimek in con.execute(sql,[id_st]):
        return priimek[0]

def datum_rojstva(id_st):
    '''funkcija vrne datum rojstva zapornika z id-jem id'''
    sql = '''SELECT datum_rojstva
            FROM osebe
            WHERE id = ?'''
    for datum in con.execute(sql,[id_st]):
        return datum[0]
def spol(id_st):
    '''funkcija vrne spol zapornika z id-jem id'''
    sql = '''SELECT spol
            FROM osebe
            WHERE id = ?'''
    for spol in con.execute(sql,[id_st]):
        return spol[0]
def kje_spi(id_st):
    '''funkcija vrne številko celice v kateri spi zapornik
       t id-jem id'''
    sql = '''SELECT celica
            FROM osebe
            WHERE id = ?'''
    for celica in con.execute(sql,[id_st]):
        return celica[0]
def max_id_zapornika():
    sql = '''SELECT MAX(id) FROM osebe'''
    return con.execute(sql).fetchone()[0]

# funkcije o celicah
def proste_moske_celice():
    '''vrne seznam tistih moskih celic, ki imajo se kako prosto mesto'''
    sql = ''' SELECT st_celice
              FROM celica
              WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  ) > 0
              AND tip LIKE 'M' '''
    sezCelic = []
    for celica in con.execute(sql):
        sezCelic.append(celica[0])
    if len(sezCelic) == 0:
        return 'Ni prostih moških celic!'
    return sezCelic

def proste_zenske_celice():
    '''vrne seznam tistih zenskih celic, ki imajo se kako prosto mesto'''
    sql = ''' SELECT st_celice
              FROM celica
              WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  ) > 0
              AND tip LIKE 'F' '''
    sezCelic = []
    for celica in con.execute(sql):
        sezCelic.append(celica[0])
    if len(sezCelic) == 0:
        return 'Ni prostih ženskih celic!'
    return sezCelic

def kdo_je_v_celici(st_celice):
    ''' funkcija vrne id-je tistih, ki spijo z zapornikom'''
    sql = '''SELECT id      
             FROM osebe
             WHERE celica = ?        
            '''
    vCelici = []
    for id_zapornika in con.execute(sql, [st_celice]):
        vCelici.append(ime(id_zapornika[0]))
    return vCelici

# funkcije o delu
def vsa_prosta_dela():
    '''funkcija vrne slovar, kjer je kljuc delo, vrednost pa prosta mesta'''
    sql = '''SELECT (SELECT opis FROM vrsta_dela WHERE id = kaj_dela) AS delo, 
        (SELECT stevilo_mest
             FROM vrsta_dela
            WHERE id = kaj_dela)-
      count(kaj_dela) AS prosta_mesta
           FROM delo
           group BY kaj_dela'''
    slovar = {}
    for el in con.execute(sql):
        if el[1] != 0:
            slovar[el[0]] = el[1]
    return slovar

def st_prostih_mest(delo):
    '''funkcija vrne koliko prostih del pripada delu delo'''
    sql = ''' SELECT (
              SELECT stevilo_mest
              FROM vrsta_dela
              WHERE id = kaj_dela
              )- count(kaj_dela) AS prosta_mesta
              FROM delo
              WHERE kaj_dela = ?'''
    for stevilo in con.execute(sql,[delo]):
        return stevilo[0]

# dodajanje podatkov

def dodaj_zapornika(ime, priimek, datum_rojstva, spol, celica):
    '''funkcija doda novega zapornika v zapor in sicer osnovne podatke'''
    sql = ''' INSERT INTO osebe (ime, priimek, datum_rojstva, spol, celica)
              VALUES (?,?,?,?,?)'''
    con.execute(sql, [ime, priimek, datum_rojstva, spol, celica])
    con.commit()


















    
