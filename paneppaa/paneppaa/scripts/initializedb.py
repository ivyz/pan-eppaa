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
        ),
        dict(
            name= 'Luna',
            image= 'Luna_big.jpg',
            description= "Nata nel 2007. Timida, riservata, rifugge il contatto con gli uomini, ma e perfettamente socializzata con i suoi conspecifici. E stata recuperata e  quindi adottabile. Famiglia consigliata: Nucleo familiare di pochi componenti, anche con bambini.",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'medio-piccola'
        ),
        dict(
            name= 'Leo',
            image= 'Leo_big.jpg',
            description= "Dolcissimo e giocherellone, ha bisogno di sfogare le sue energie correndo nelle passeggiate con il suo futuro migliore amico. Pu stare sia in casa che in giardino, ma se viene tenuto in casa ha bisogno di essere stimolato altrimenti se la prenderà con i mobili. Consigliato per persone dinamiche.",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Dick',
            image= 'Dick_big.jpg',
            description= "Dick è arrivato da poco in canile, è in fase conoscitiva necessita quindi di preadozione",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Holly',
            image= 'Holly_big.jpg',
            description= "Spledida esemplare, perfettamente socializzata con le persone, adatta anche ai bambini purch non troppo piccoli perch  un cane esuberante. Meglio se potr essere adottata come figlia unica, senza altri cani.",
            born_year= 1,
            kind= 'Amstaff',
            taglia= 'media'
        ),
        dict(
            name= 'Marton',
            image= 'Marton_big.jpg',
            description= "Nato nel maggio 2011, attualmente  in fase di recupero per via della sua timidezza. E pauroso ma anche molto dolce. Ambiente consigliato: Esterno ma tranquillo preferibilmente non in citt. Famiglia consigliata: Adatto a famiglie anche con bambini. Limportante che sia rispettato.",
            born_year= 1,
            kind= 'Incrocio nordico',
            taglia= 'grande'
        ),
        dict(
            name= 'Rodolph',
            image= 'Rodolph_big.jpg',
            description= "Nato nel maggio 2011, attualmente in fase di recupero per via della sua timidezza. Ha un carattere indipendente. Ambiente consigliato: Esterno ma tranquillo preferibilmente non in citt. Famiglia consigliata: Non  adatto a bambini e richiede dei compagni pazienti.",
            born_year= 1,
            kind= 'Incrocio nordico',
            taglia= 'grande'
        ),
        dict(
            name= 'Birbo',
            image= 'Birbo_big.jpg',
            description= "Dolcissimo e docilissimo adora le coccole.Vive tranquillamente sia in casa che in giardino.Adatto a tutti, anche a famiglie con bambini.",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'grande'
        ),
        dict(
            name= 'Leo',
            image= 'Leo_pb_big.jpg',
            description= "Leo a dispetto della nomea dei pitbull e dolce ed affettuoso. Ambiente consigliato: Casa, o comunque in giardino con un riparo per le giornate fredde. Adatto a persone giovani. Non deve essere adottato con lintento di utilizzarlo come cane da guardia. Si cede solo a persone consapevoli della razza e che lo sappiano gestire. No anziani e bambini piccoli.",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'grande'
        ),
        dict(
            name= 'Dora',
            image= 'Dora_big.jpg',
            description= "Molto paurosa e diffidente. Se prende confidenza con chi la segue si trasforma in dolce ed affettuosa Ambiente consigliato: Posto molto tranquillo Famiglia consigliata: Nucleo familiare ristretto, adatta soprattutto ad anziani in quanto e un cane da compagnia. Necessita di incontri conoscitivi",
            born_year= 1,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Norton',
            image= 'Norton_big.jpg',
            description= "Norton e il tipico caso clinico dei testi di scienze comportamentali. Uno specifico protocollo di recupero e riuscito a fortificarlo per le sue innate paure nei confronti delle persone che rimangono tuttavia molto elevate. Ambiente consigliato: appartamento in luogo tranquillo. Necessita di incontri conoscitivi",
            born_year= 1,
            kind= 'Segugio',
            taglia= 'media'
        ),
        dict(
            name= 'Pippo',
            image= 'Pippo_big.jpg',
            description= "Nato il 01/12/2007. E stato recupertato ed e adottabile, ha davvero molto bisogno di coccole, unico motivo per cui rimane in canile e la sua mole. Ambiente consigliato: Giardino, per via della sua mole.",
            born_year= 1,
            kind= 'Incrocio pastore Asia Centrale',
            taglia= 'gigante'
        ),
        dict(
            name= 'Ali e Saba',
            image= 'Ali_Saba_big.jpg',
            description= "Hanno sempre vissuto insieme, adottati proprio dal nostro canile, molto tempo fa, sono stati da poco nuovamente ceduti. Ormai sono anziani ed  necessario adottarli insieme. Sono molto timidi.",
            born_year= 1,
            kind= 'Husky',
            taglia= 'medio-grande'
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
