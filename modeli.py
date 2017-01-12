import sqlite3
import datetime
con = sqlite3.connect('BazaZapor.db')


def ime(id):
    '''funckija vrne ime zapornika z id-jem id'''
    sql = '''SELECT ime
            FROM osebe
            WHERE id = ?'''
    for ime in con.execute(sql,[id]):
        return ime[0]

def priimek(id):
    '''funckija vrne priimek zapornika z id-jem id'''
    sql = '''SELECT priimek
            FROM osebe
            WHERE id = ?'''
    for priimek in con.execute(sql,[id]):
        return priimek[0]

def datum_rojstva(id):
    '''funkcija vrne datum rojstva zapornika z id-jem id'''
    sql = '''SELECT datum_rojstva
            FROM osebe
            WHERE id = ?'''
    for datum in con.execute(sql,[id]):
        return datum[0]
def spol(id):
    '''funkcija vrne spol zapornika z id-jem id'''
    sql = '''SELECT spol
            FROM osebe
            WHERE id = ?'''
    for spol in con.execute(sql,[id]):
        return spol[0]

def kje_spi(id):
    '''funkcija vrne številko celice v kateri spi zapornik
       t id-jem id'''
    sql = '''SELECT celica
            FROM osebe
            WHERE id = ?'''
    for celica in con.execute(sql,[id]):
        return celica[0]

def max_id_zapornik():
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


###########################################################################
#                                                                         #
#                           KAZNI ZAPORNIKA                               #
#                                                                         #
###########################################################################

def kdaj_iz_zapora(zacetniDatum, trajanje):
    ''' Funkcija vrne datum, ko bo zapornik šel iz zapora'''
    slovar = {1: 31 , 2: 28, 3 : 31, 4:30, 5:31, 6:30,
            7:31, 8:31, 9: 30, 10: 31, 11:30, 12:31}
    
    stDni = trajanje
    datum = zacetniDatum.split('-')
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
        vTaMesec = vTemMesecu - treDan + 1
        if vTaMesec <= stDni:
            # torej bomo skočili na naslendji mesec
            treDan = 1
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
    date = str(leto) + '-' + str(treMesec) +  '-' + str(treDan)
    return date

def kazni_zapornika(id):
    '''funkcija vrne seznam kazni, ki jih je zapornik naredil
       predpostavka: baza je zgrajena v principu na pravilen nacin:
       datumi se ne prekrivajo'''
    # vzamemo le zadnji datum v bazi in tiste kazni, ki imajo ta datum
    # datumi pred maximalnim datumom: to so tisti datumi, ki se nanašajo na prejšnje areste
    sql2 = '''SELECT MAX(datum_prihoda) FROM zlocin WHERE zlocinec = ?'''
    datum = con.execute(sql2, [id]).fetchone()[0]
    print(datum)
    sql1 = '''SELECT vrsta_zlocin, trajanje FROM zlocin WHERE zlocinec = ? AND datum_prihoda = ?'''
    
    slovar = {}
    i = 1
    for kazen in con.execute(sql1,[id, datum]):       
        slovar[i] = [kazen[0], kazen[1]]
        i += 1
    return slovar

def datum_aresta(id):
    '''funkcija vrne datum aresta zapornika z id-jem id'''
    sql = '''SELECT MAX(datum_prihoda) FROM zlocin WHERE zlocinec = ?'''
    zacDatum = con.execute(sql, [id]).fetchone()[0]
    slovar = {}
    i = 0
    slovarKazni = kazni_zapornika(id)
    for st_kazni in slovarKazni:
        trajanje = slovarKazni[st_kazni][1]
        kazen = slovarKazni[st_kazni][0]
        konDatum = kdaj_iz_zapora(zacDatum, trajanje)
        slovar[i] = [kazen, zacDatum, konDatum]
        zacDatum = konDatum
        i += 1
    return slovar
        
def vse_kazni(id):
    ''' funkcija vrne vse kazni, ki jih je zapornik naredil'''
    sql = '''SELECT DISTINCT datum_prihoda FROM zlocin WHERE zlocinec = ?'''
    sezDatumov = []
    for datumPrihoda in  con.execute(sql, [id]):
        sezDatumov.append(datumPrihoda[0])

    i = 1
    slovar = {}
    for datum in sezDatumov:
        zacDatum = datum
        sql1 = '''SELECT vrsta_zlocin, trajanje FROM zlocin WHERE zlocinec = ? AND datum_prihoda = ?'''
        kazni = con.execute(sql1,[id, datum]).fetchall()
        for par in kazni:
            kazen = par[0]
            trajanje = par[1]
            konDatum = kdaj_iz_zapora(zacDatum, trajanje)
            slovar[i] = [kazen, zacDatum, konDatum]
            zacDatum = konDatum
            i += 1
    return slovar










    
