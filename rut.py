from bottle import route, run, template, request, get, post, redirect
import modeli

@route('/')
def index():
    return template('zacetna_stran')



#######################    ZAPORNIKI   #######################################################################################################################################################################
@route('/zaporniki/')
def zaporniki():
    return template('zaporniki')

@route('/zaporniki/poisci/')
def zaporniki_poisci():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if modeli.id_je_v_bazi(id_zapornika):
            return template('zaporniki_poisci', ime = modeli.ime(id_zapornika), priimek = modeli.priimek(id_zapornika), datum_rojstva = modeli.datum_rojstva(id_zapornika), spol = modeli.spol(id_zapornika), celica = modeli.kje_spi(id_zapornika))
        else:
            return template('zaporniki_poisci', ime = None, vnos = vnos)
    except:
        return template('zaporniki_poisci', ime = None, vnos = vnos)

@route('/zaporniki/poisciVsi/')
def zaporniki_poisciVsi():
    ime = str(request.query.ime)
    priimek = str(request.query.priimek)
    datum_rojstva = str(request.query.datum_rojstva)
    spol = str(request.query.spol)
    return template('zaporniki_poisciVsi', zaporniki = modeli.poisci_zapornika(ime, priimek, datum_rojstva, spol))

@route('/zaporniki/kazniva_dejanja/')
def zaporniki_kazniva_dejanja():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if modeli.id_je_v_bazi(id_zapornika):
            return template('zaporniki_kazniva_dejanja', kazni = modeli.vse_kazni(id_zapornika))
        else:
            return template('zaporniki_kazniva_dejanja', vnos = vnos, kazni = None)
    except:
        return template('zaporniki_kazniva_dejanja', vnos = vnos, kazni = None)

@route('/zaporniki/finance/')
def zaporniki_finance():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if modeli.id_je_v_bazi(id_zapornika):
            return template('zaporniki_finance', delo = modeli.zasluzki_zapornika(id_zapornika), zasluzek = modeli.zasluzki_pred_po_arestu(id_zapornika), dolzanPo = modeli.dolzan(id_zapornika), dolzanPred = modeli.dolzan_pred_arestom(id_zapornika))
        else:
            return template('zaporniki_finance', vnos = vnos, delo  = None )
    except:
        return template('zaporniki_finance', vnos = vnos, delo = None)

@route('/zaporniki/delo/')
def zaporniki_delo():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if modeli.id_je_v_bazi(id_zapornika):
            return template('zaporniki_delo', delo = modeli.zasluzki_zapornika(id_zapornika))
        else:
            return template('zaporniki_delo', vnos = vnos, delo  = None )
    except:
        return template('zaporniki_delo', vnos = vnos, delo = None)


@route('/zaporniki/dodaj/')
def zaporniki_dodaj():
    return template('zaporniki_dodaj')

@post('/zaporniki/dodaj/')
def zaporniki_dodaj_submit():
    #v bazo dodamo zapornika
    ime = str(request.forms.get('ime'))
    priimek = str(request.forms.get('priimek'))
    datum_rojstva = str(request.forms.get('datum_rojstva')).split('-')
    datum_rojstva = datum_rojstva[2] + '/' + datum_rojstva[1] + '/' + datum_rojstva[0]
    spol = str(request.forms.spol)
    #v bazo dodamo kazen
    trajanje = str(request.forms.get('trajanje'))
    pomilostitev = str(request.forms.get('pomilostitev'))
    denarna_kazen = str(request.forms.get('denarna_kazen'))
    vrsta_zlocina = str(request.forms.get('vrsta_zlocina'))
    if modeli.dodaj_zapornika(ime, priimek, datum_rojstva, spol)!=None:
        modeli.dodaj_zlocin(modeli.max_v_bazi(), float(trajanje), pomilostitev, float(denarna_kazen), vrsta_zlocina)
    redirect('/zaporniki/dodaj/')

@route('/zaporniki/dodaj_kazen/')
def zaporniki_dodaj_kazen():
    return template('zaporniki_dodaj_kazen')

@post('/zaporniki/dodaj_kazen/')
def zaporniki_dodaj_kazen_submit():
    id_zapornika = str(request.forms.get('id_zapornika'))
    #v bazo dodamo kazen
    trajanje = str(request.forms.get('trajanje'))
    pomilostitev = str(request.forms.get('pomilostitev'))
    denarna_kazen = str(request.forms.get('denarna_kazen'))
    vrsta_zlocina = str(request.forms.get('vrsta_zlocina'))
    modeli.dodaj_zlocin(id_zapornika, float(trajanje), pomilostitev, float(denarna_kazen), vrsta_zlocina)
    redirect('/zaporniki/dodaj_kazen/')



#######################    CELICE   #######################################################################################################################################################################

@route('/celice/')
def celice():
    return template('celice')

@route('/celice/poisci/')
def celice_poisci():
    vnos = str(request.query.st_celice)
    zaporniki = modeli.kdo_je_v_celici(vnos)
    if zaporniki == []:
        return template('celice_poisci', zaporniki = None, vnos = vnos)
    else:
        return template('celice_poisci', zaporniki = zaporniki)

@route('/celice/proste/')
def celice_proste():
    return template('celice_proste', moske = modeli.proste_moske_celice(), zenske = modeli.proste_zenske_celice())

@route('/celice/zamenjaj/')
def celice_zamenjaj():
    return template('celice_zamenjaj')

@post('/celice/zamenjaj/')
def celice_zamenjaj_submit():
    try:
        modeli.prestavi_zapornika(int(request.forms.get('id_zapornika')), int(request.forms.get('st_celice')))
    except:
        pass
    redirect('/celice/zamenjaj/')



#######################    DELO   #######################################################################################################################################################################

@route('/delo/')
def delo():
    return template('delo')

@route('/delo/prosto/')
def delo_prosto():
    return template('delo_prosto', vsa_prosta = modeli.prosta_dela_danes(), urne_postavke = modeli.urne_postavke())

@post('/delo/prosto/')
def delo_prosto_submit():
    try:
        modeli.dodaj_delo(int(request.forms.get('id_zapornika')), str(request.forms.get('delo')), int(request.forms.get('st_ur')))
    except:
        pass
    redirect('/delo/prosto/')

##@route('/delo/zgodovina/')
##def delo_zgodovina():
##    return template('delo_zgodovina', zgodovina = None)

@route('/delo/zgodovina/')
def delo_zgodovina_submit():
    return template('delo_zgodovina', zgodovina = modeli.preteklo_delo(str(request.query.zacetek), str(request.query.konec)) )

run(debug = True, refresh = True)  
