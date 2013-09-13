import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Dog,
    Base,
    Event,
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
        '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    from datetime import date

    with transaction.manager:
        dogs = [dict(
            name = 'Terry',
            image = 'Terry_big.jpg',
            description = "Cane buonissimo, ha estremo bisogno di coccole, tira un po al guinzaglio ma siamo sicuri che si abituer se avr la possibilit di sfogare le sue energie.",
            born_year = 3,
            taglia =  'medio-grande',
            kind = 'Labrador'
        ),
        dict(
            name= 'Balto',
            image= 'Balto_big.jpg',
            description= "Il bellissimo Balto, ma anche molto diffidente, ha bisogno di incontri conoscitivi.",
            born_year= 4,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Bal',
            image= 'Balu_big.jpg',
            description= "Taglia quasi gigante, il nostr Bal da molto tempo al canile,  possessivo con il cibo e con i suoi giochi. Necessita di incontri conoscitivi.",
            born_year= 8,
            kind= 'Labrador',
            taglia= 'grande'
        ),
        dict(
            name= 'Alba',
            image= 'Alba_big.jpg',
            description= "La spaventatissima Alba ha bisogno di un compagno paziente del quale potersi fidare, lambiente ideale un posto tranquillo lontano dai rumori della citt",
            born_year= 4,
            kind= 'Incrocio labrador',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Feo',
            image= 'Feo_big.jpg',
            description= "Feo  attualmente in fase di recupero perch non socializza bene con tutte le persone",
            born_year= 8,
            kind= 'San Bernardo',
            taglia= 'gigante'
        ),
        dict(
            name= 'Spina',
            image= 'Spina_big.jpg',
            description= "Piccola spina, ti fiderai mai di qualcuno Se qualcuno  molto paziente da rispettare le tue paure forse si...",
            born_year= 7,
            kind= 'Incrocio spinone',
            taglia= 'medio-piccola'
        ),
        dict(
            name= 'Stuard',
            image= 'Stuard_big.jpg',
            description= "Stuard  un po la mascotte del canile, attualmente  il pi vecchio, ma anche il pi coccolone. Leggermente ipovedente, non va forzato troppo nelle passeggiate.",
            born_year= 10,
            kind= 'Meticcio',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Black',
            image= 'Black_big.jpg',
            description= "Black  dolcissimo con chi conosce, e diffidente con chi non conosce. Necessita di incontri conoscitivi",
            born_year= 6,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Bonnie',
            image= 'Bonnie_big.jpg',
            description= "A dispetto della nomea del Pitbull  dolcissima e coccolosissima. Cediamo solo a persone consapevoli della razza.",
            born_year= 35,
            kind= 'Pitbull',
            taglia= 'media'
        ),
        dict(
            name= 'Eddy',
            image= 'Eddy_big.jpg',
            description= "Bellissimo Eddy ma molto attaccato al canile perch arriva da una brutta situazione. Necessita quindi di incontri conoscitivi per potersi adattare bene nella sua nuova casa. Necessita quindi di incontri conoscitivi per potersi adattare bene nella sua nuova casa. Necessita quindi di incontri conoscitivi per potersi adattare bene nella sua nuova casa.",
            born_year= 1,
            kind= 'Incrocio da pastore',
            taglia= 'grande'
        )];

        for dog in dogs:
            d = Dog(name=dog['name'], born_year=dog['born_year'],
                description=dog['description'], image=dog['image'],
                kind=dog['kind'], size=dog['taglia'])
            DBSession.add(d)

    with transaction.manager:
        events = [dict(
            title = 'Paes dei presepi',
            description = "Cane buonissimo, ha estremo bisogno di coccole, tira un po al guinzaglio ma siamo sicuri che si abituer se avr la possibilit di sfogare le sue energie.",
            date = date(2012, 12, 25)
        ),
        dict(
            title = 'Mercatino',
            description = "Cane buonissimo, ha estremo bisogno di coccole, tira un po al guinzaglio ma siamo sicuri che si abituer se avr la possibilit di sfogare le sue energie.",
            date = date(2013, 7, 8)
        ),
        dict(
            title = 'Porte aperte',
            description = "Cane buonissimo, ha estremo bisogno di coccole, tira un po al guinzaglio ma siamo sicuri che si abituer se avr la possibilit di sfogare le sue energie.",
            date = date(2013, 10, 6)
        )];

        for evt in events:
            e = Event(title=evt['title'], date=evt['date'],
                      description=evt['description'])
            DBSession.add(e)
