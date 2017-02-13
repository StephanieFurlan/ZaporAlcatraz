import sqlite3
import datetime
con = sqlite3.connect('BazaZapor.db')

###########################################################################
#                                                                         #
#                           OSEBNI PODATKI ZAPORNIKA                      #
#                                                                         #
###########################################################################

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
        if spol[0] == 'M':
            return 'Moški'
        return 'Ženski'
        

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

def id_je_v_bazi(id):
    '''Funkcija vrne True ali False glede na to, če id je v bazi'''
    sql = '''SELECT id FROM osebe'''
    sezID = []
    for idVBazi in con.execute(sql):
        sezID.append(idVBazi[0])
    # pogledamo če id je v bazi
    if id in sezID:
        return True
    return False

def poisci_zapornika(ime, priimek, datum_rojstva, spol):
    ''' funkcija poisce zapornike, ki imajo skupne podatke ime, priimek, datum_rojstva, spol'''
    datum = datum_rojstva.split('-')
    if len(datum) == 3:
        datum_rojstva = datum[2] + '/' + datum[1] + '/' + datum[0]
    '''funkcija poisce zapornika z zgornjimi podatki'''
    sql =''' SELECT id, ime, priimek, datum_rojstva, spol FROM osebe WHERE ime LIKE ? AND priimek LIKE ?
         AND datum_rojstva LIKE ? AND spol LIKE ? '''
    sezOseb = []
    for a, i,p,d,s in con.execute(sql, ['%'+ime+'%', '%'+priimek+'%', '%'+datum_rojstva+'%', '%'+spol+'%']):
        sezOseb.append([a, i,p,d,s])
    return sezOseb
        

###########################################################################
#                                                                         #
#                           O CELICAH                                     #
#                                                                         #
###########################################################################

def proste_moske_celice():
    '''vrne seznam tistih moskih celic, ki imajo se kako prosto mesto'''
    sql = '''SELECT st_celice,
       velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  )
  FROM celica
 WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  )
>      0 AND 
       tip LIKE 'M' ''';

    sezCelic = []
    for celica, velikost in con.execute(sql):
        sezCelic.append([celica, velikost])
    if len(sezCelic) == 0:
        return 'Ni prostih moških celic!'
    return sezCelic

def proste_zenske_celice():
    '''vrne seznam tistih zenskih celic, ki imajo se kako prosto mesto'''
    sql = '''SELECT st_celice,
       velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  )
  FROM celica
 WHERE velikost - (
                      SELECT count(celica) 
                        FROM OSEBE
                       WHERE celica = st_celice
                  )
>      0 AND 
       tip LIKE 'F' ''';
    sezCelic = []
    for celica, velikost in con.execute(sql):
        sezCelic.append([celica, velikost])
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
        vCelici.append([datum_zadnjega_aresta(id_zapornika[0]),id_zapornika[0] ,ime(id_zapornika[0]) , priimek(id_zapornika[0])])
    return vCelici


###########################################################################
#                                                                         #
#                           DELO                                          #
#                                                                         #
###########################################################################

def dodaj_delo(id, kaj_dela, st_ur):
    '''funkcija doda podatke o delu delavcu na danasnji dan'''
    sql = '''INSERT INTO delo (delavec, kaj_dela, stevilo_ur, datum)
             VALUES(?,?,?,?)'''
    sqlKajDela = '''SELECT id FROM vrsta_dela WHERE opis = ?'''
    # delo dadamo v bazo le, če je celo stevilo in je med 0 in 8
    if isinstance(st_ur, int):
        if kaj_dela in prosta_dela_danes().keys():
            if 0 < st_ur <= 8:
                id_dela = con.execute(sqlKajDela,[kaj_dela]).fetchone()[0]
                datum = str(datetime.datetime.now()).split(' ')[0]
                con.execute(sql, [id, id_dela, st_ur, datum])
                con.commit()


def prosta_dela_danes():
    danes = str(datetime.datetime.now()).split(' ')[0]
    sql = '''SELECT id, opis, (stevilo_mest - (SELECT COUNT(kaj_dela) FROM delo WHERE kaj_dela = vrsta_dela.id AND delo.datum = ?))
             AS prosta_dela FROM vrsta_dela '''
    slovarProstihDel = {}
    for a, delo, st_mest in con.execute(sql, [danes]).fetchall():
        if int(st_mest) != 0:
            slovarProstihDel[delo] = st_mest
    return slovarProstihDel


def urne_postavke():
    sql = '''SELECT opis, urna_postavka FROM vrsta_dela'''
    ure = {}
    for opis, urna_postavka in con.execute(sql):
        ure[opis] = urna_postavka
    return ure

def preteklo_delo(zac_datum, kon_datum):
    ''' funkcija vrne vsa dela na intervalu zac-kon'''
    sql = '''SELECT datum, delavec, (SELECT opis FROM vrsta_dela WHERE vrsta_dela.id = kaj_dela) AS delo,
          stevilo_ur, stevilo_ur * (SELECT urna_postavka FROM vrsta_dela WHERE vrsta_dela.id = kaj_dela) AS zasluzek
          FROM delo WHERE datum  BETWEEN ? AND ? '''
    sezDel = []
    for (datum, delavec, delo, stevilo_ur, zasluzek) in con.execute(sql, [zac_datum, kon_datum]):
        sezDel.append([datum, delavec, delo, stevilo_ur, float("{0:2f}".format(round(zasluzek,2)))])
    return sezDel

def delo_zapornika(id):
    '''funkcija vrne vse informacije o delu zapornika z id-je id'''
    pass

###########################################################################
#                                                                         #
#                           FINANCE ZAPORNIKA                             #
#                                                                         #
# OPIS: 
###########################################################################

def zasluzki_zapornika(id):
    '''funkcija vrne seznam,sestavljen iz dveh sezanomov:
       1. podatki dela pred zadnjim arestom
       2. podatki dela po zadnjem arestu
       kjer je vsak element seznam oblike
       [id_dela, datum, vrsta_dela, st_ur, zasluzek]'''
    sql = '''SELECT id, kaj_dela, stevilo_ur, datum FROM delo WHERE delavec = ?'''
    sezDel = []
    sezPred = []
    sezPo = []
    for cetvorka in con.execute(sql, [id]).fetchall():
        
        id_dela = cetvorka[0]
        sqlDela = '''SELECT opis, urna_postavka FROM vrsta_dela WHERE id = ?'''
        o_delu = con.execute(sqlDela, [cetvorka[1]]).fetchone()
        delo = o_delu[0]
        urna_postavka = o_delu[1]
        st_ur = cetvorka[2]
        zasluzek = float("{0:.2f}".format(round(st_ur * urna_postavka,2)))
        datum = cetvorka[3]
        zadnji_arest = datum_zadnjega_aresta(id)
        if datum < zadnji_arest:
            sezPred.append([id_dela, datum, delo, st_ur, zasluzek])
        else:
            sezPo.append([id_dela, datum, delo, st_ur, zasluzek])
    sezDel.append(sezPred)
    sezDel.append(sezPo)
    return sezDel

def zasluzki_pred_po_arestu(id):
    '''funkcija vrne vsoto vseh zasluzkov zapornika
       '''
    zasluzekPred = 0
    zasluzekPo = 0
    sezPred, sezPo = zasluzki_zapornika(id)
    for cetvorka in sezPred:
        zasluzekPred += cetvorka[4]
    for cetvorka in sezPo:
        zasluzekPo += cetvorka[4]
    return [zasluzekPred, zasluzekPo]

def dolzan(id):
    '''funkcija vrne koliko je zapornik dolzan, po zadnjem arestu'''
    zadnji_arest = datum_zadnjega_aresta(id)
    sql = '''SELECT denarna_kazen FROM zlocin WHERE zlocinec = ? AND datum_prihoda = ?'''
    vsota = 0
    for koliko in con.execute(sql, [id, zadnji_arest]).fetchall():
        vsota += koliko[0]
    return vsota

def dolzan_pred_arestom(id):
    '''funkcija vrne koliko denarja je bil dolzan zapornik pred arestom, to
       je ce je kdaj bil  zapou prej'''
    sql = '''SELECT denarna_kazen FROM zlocin WHERE zlocinec = ? AND datum_prihoda < ?'''
    zadnji_arest = datum_zadnjega_aresta(id)
    vsota = 0
    for koliko in con.execute(sql, [id, zadnji_arest]).fetchall():
        vsota += koliko[0]
    return vsota

def datum_zadnjega_aresta(id):
    '''vrne datum zadnjega aresta'''
    sql = '''SELECT MAX(datum_prihoda) FROM zlocin WHERE zlocinec = ?'''
    return con.execute(sql,[id]).fetchone()[0]

        


###########################################################################
#                                                                         #
#                           DODAJANJE V BAZO                              #
#                                                                         #
###########################################################################

def dodaj_zapornika(ime, priimek, datum_rojstva, spol):
    '''funkcija doda novega zapornika v zapor in sicer osnovne podatke'''
    sql = ''' INSERT INTO osebe (ime, priimek, datum_rojstva, spol, celica)
              VALUES (?,?,?,?,?)'''
    # zapornika nastavimo v prvo prosto celico
    if spol == 'M':
        celica = proste_moske_celice()[0][0]
    else:
        celica = proste_zenske_celice()[0][0]
    # pogledamo da je datum rojstva tak, da ima zapornik vsaj 100 let
    # letnica 1917
    leto = int(datum_rojstva.split('/')[2])
    danes = int(str(datetime.datetime.now()).split('-')[0])
    if 1917 <= leto <=  int(danes) - 20:
        con.execute(sql, [ime, priimek, datum_rojstva, spol, celica])
        con.commit()
    else:
        return None


def dodaj_zlocin(id_zapornika, trajanje, pomilostitev, denarna_kazen, vrsta_zlocin):
    ''' funkcija doda podatke o kaznivih dejanjih zlocinca z id-jem id'''
    # pazimo, da sta denarna_kazen in trajanje pozitivni stevili!
    if isinstance(trajanje/1, float) and isinstance(denarna_kazen/1, float):
        if trajanje > 0 and denarna_kazen > 0:
            datum_prihoda = str(datetime.datetime.now()).split()[0]
            sql2 = '''INSERT INTO zlocin (zlocinec, datum_prihoda, trajanje, pomilostitev, denarna_kazen, vrsta_zlocin)
                      VALUES (?,?,?,?,?,?)'''
            con.execute(sql2,[id_zapornika, datum_prihoda, trajanje, pomilostitev, denarna_kazen, vrsta_zlocin])
            con.commit()
    else:
        return None

def prestavi_zapornika(id_zapornika, nova_celica):
    '''funkcija prestavi zapornika v ćeleno celico'''
    s = spol(id_zapornika)
    if s == 'Moški':
        proste = proste_moske_celice()
    else:
        proste = proste_zenske_celice()
    sezProstih = []
    for st_celice, st_mest in proste:
        sezProstih.append(st_celice)
    if nova_celica in sezProstih:
        sql = '''UPDATE osebe SET celica = ? WHERE id = ?'''
        con.execute(sql,[nova_celica, id_zapornika])
        con.commit()
    else:
        return False


def max_v_bazi():
    sql = '''SELECT MAX(id) FROM osebe'''
    return con.execute(sql).fetchone()[0]

    
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
    '''funkcija vrne slovar kazni, ki jih je zapornik naredil
       predpostavka: baza je zgrajena v principu na pravilen nacin:
       datumi se ne prekrivajo. Slovar vsebuje tiste kazni, za katere je
       zapornik sedaj v zaporu. Slovar ima:
       * kljuc = stevilo kazni: to je po vrsti 1,2,3...
       * vrednsot = seznam oblike [kazen, trajanje]'''
    # vzamemo le zadnji datum v bazi in tiste kazni, ki imajo ta datum
    # datumi pred maximalnim datumom: to so tisti datumi, ki se nanašajo na prejšnje areste
    sql2 = '''SELECT MAX(datum_prihoda) FROM zlocin WHERE zlocinec = ?'''
    datum = con.execute(sql2, [id]).fetchone()[0]
    sql1 = '''SELECT vrsta_zlocin, trajanje FROM zlocin WHERE zlocinec = ? AND datum_prihoda = ?'''
    
    slovar = {}
    i = 1
    for kazen in con.execute(sql1,[id, datum]):       
        slovar[i] = [kazen[0], kazen[1]]
        i += 1
    return slovar

def datum_aresta(id):
    '''funkcija vrne slovar:
       kljuc = stevilo kazni, 1,2,3 koliko jih je naredil
       vrednost = seznam oblike ['''
    sql = '''SELECT MAX(datum_prihoda) FROM zlocin WHERE zlocinec = ?'''
    zacDatum = con.execute(sql, [id]).fetchone()[0]
    slovar = {}
    i = 1
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
        sql1 = '''SELECT id, vrsta_zlocin, trajanje FROM zlocin WHERE zlocinec = ? AND datum_prihoda = ?'''
        kazni = con.execute(sql1,[id, datum]).fetchall()
        for par in kazni:
            id_kazni = par[0]
            kazen = par[1]
            trajanje = par[2]
            
            konDatum = kdaj_iz_zapora(zacDatum, trajanje)
            slovar[i] = [id_kazni, kazen, zacDatum, konDatum]
            zacDatum = konDatum
            i += 1
    return slovar


###########################################################################
#                                                                         #
#                           UREJEVANJE                                    #
#                                                                         #
###########################################################################


def zamenjaj_ime_zapornika(id, ime):
    ''' funkcija spremeni v bazi ime zapornika z id-jem id'''
    sql = ''' UPDATE osebe SET ime = ? WHERE id = ? '''
    con.execute(sql, [ime, id])
    con.commit()



###########################################################################
#                                                                         #
#                           POMOŽNE FUNKCIJE                              #
#                                                                         #
###########################################################################







    
