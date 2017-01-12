from bottle import route, run, template, request, get, post
import modeli

@route('/')
def index():
    return template('zacetna_stran')

@route('/zaporniki/')
def zaporniki():
    return template('zaporniki')

@route('/zaporniki_poisci/')
def zaporniki_poisci():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if 0 < id_zapornika <= int(modeli.max_id_zapornika()):
            return template('zaporniki_poisci', ime = modeli.ime(id_zapornika), priimek = modeli.priimek(id_zapornika), datum_rojstva = modeli.datum_rojstva(id_zapornika), spol = modeli.spol(id_zapornika), celica = modeli.kje_spi(id_zapornika))
        else:
            return template('zaporniki_poisci', ime = None, vnos = vnos)
    except:
        return template('zaporniki_poisci', ime = None, vnos = vnos)

@route('/zaporniki_kazniva_dejanja/')
def zaporniki_kazniva_dejanja():
    vnos = str(request.query.id_zapornika)
    try:
        id_zapornika = int(vnos)
        if 0 < id_zapornika <= int(modeli.max_id_zapornika()):
            return template('zaporniki_kazniva_dejanja', vnos = None)
        else:
            return template('zaporniki_kazniva_dejanja', vnos = vnos)
    except:
        return template('zaporniki_kazniva_dejanja', vnos = vnos)    
        
@route('/celice/')
def celice():
    return template('celice')

@route('/delo/')
def delo():
    return template('delo')

run()

