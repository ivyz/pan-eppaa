#!/usr/bin/python
# -*- coding: utf-8 -*-
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
    News
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
            description = u'Cane buonissimo, ha estremo bisogno di coccole, tira un po al guinzaglio ma siamo sicuri che si abituerà se avrà la possibilità di sfogare le sue energie in passeggiate giornaliere e giochi con il suo amico umano. E\' senza dubbio un cane esuberante ma affettuoso, non è adatto a bambini ed anziani proprio per la sua esuberanza.',
            born_year = 2008,
            taglia =  'medio-grande',
            kind = 'Labrador'
        ),
        dict(
            name= 'Balto',
            image= 'Balto_big.jpg',
            description= u'Il bellissimo Balto, ha bisogno di incontri conoscitivi in quanto si trova da molto tempo al canile. E\' molto giocherellone, affettuoso ed ha bisogno di stimoli nel gioco e nell\'approcio con le persone. E\' molto possessivo sia con gli oggetti che con il cibo. Il suo ambiente ideale è il giardino in un posto tranquillo, lontano dai centri abitati. E\' adatto a persone che amano le camminate e che lo facciano sfogare. Cane non adatto a bambini ed anziani. Preferibili incontri conoscitivi.',
            born_year= 2007,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= u'Balù',
            image= 'Balu_big.jpg',
            description= u'Taglia quasi gigante, il nostro Balù è da molto tempo al canile, possessivo con il cibo e con i suoi giochi (guai a chi tocca il suo Pluto!). Necessita di incontri conoscitivi. Va tenuto al calduccio perché ormai ha la sua bell\'età. Non adatto a bambini ed anziani per via della sua mole.',
            born_year= 2006,
            kind= 'Labrador',
            taglia= 'grande'
        ),
        dict(
            name= 'Alba',
            image= 'Alba_big.jpg',
            description= u'La spaventatissima Alba ha bisogno di un compagno paziente del quale potersi fidare, che sia disposto a degli incontri conoscitivi. La sua casa ideale è un posto tranquillo lontano dai rumori della città. E\' adatta a famiglie non numerose.',
            born_year= 2008,
            kind= 'Incrocio labrador',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Feo',
            image= 'Feo_big.jpg',
            description= u'Feo è attualmente in fase di recupero perchè non socializza bene con tutte le persone, probabilmente è stato poco o mal socializzato ed anche il canile ha influito sul suo umore.',
            born_year= 2005,
            kind= 'San Bernardo',
            taglia= 'gigante'
        ),
        dict(
            name= 'Spina',
            image= 'Spina_big.jpg',
            description= u'Piccola spina, ti fiderai mai di qualcuno? Se qualcuno sarà abbastanza paziente da rispettare i tuoi tempi e calmare le tue paure forse si... E\' molto buona e ben socializzata con i suoi simili ma rifugge il contatto con le persone.',
            born_year= 2005,
            kind= 'Incrocio spinone',
            taglia= 'medio-piccola'
        ),
        dict(
            name= 'Stuard',
            image= 'Stuard_big.jpg',
            description= u'Stuard è un po\' la mascotte del canile, attualmente  il più vecchio, ma anche il più coccolone. Leggermente ipovedente, attenzione che non scambi il dito con un biscotto! Non va forzato troppo nelle passeggiate e va tenuto al calduccio, l\'appartamento è il suo ambiente naturale!',
            born_year= 2004,
            kind= 'Meticcio',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Black',
            image= 'Black_big.jpg',
            description= u'Black è dolcissimo con chi conosce, e diffidente con chi non conosce. Non è un cane che ama la troppa manipolazione, quando vorrà le coccole sarà lui a chiederle. Necessita di incontri conoscitivi e deve essere trattato con rispetto. E\' un ottimo cane da appartamento, non adatto a bambini e anziani.',
            born_year= 2006,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Bonnie',
            image= 'Bonnie_big.jpg',
            description= u'A dispetto della nomea del Pitbull è dolcissima e coccolosissima. Adatta a persone giovani. Non deve essere adottata con l\'intento di utilizzarla come cane da guardia. Si cede solo a persone consapevoli della razza e che la sappiano gestire. Non adatta ad anziani e bambini piccoli. Per il suo pelo raso va tenuta al riparo in inverno.',
            born_year= 2006,
            kind= 'Pitbull',
            taglia= 'media'
        ),
        dict(
            name= 'Eddy',
            image= 'Eddy_big.jpg',
            description= u'Bellissimo Eddy ma molto attaccato al canile perchè arriva da una brutta situazione. Necessita quindi di incontri conoscitivi per potersi adattare bene nella sua nuova casa. Ha un carattere vivace, esuberante, sicuro di se ed emotivo. Deve essere saputo gestire quindi sconsigliamo bambini ed anziani anche per la sua mole. Il suo pelo folto gli permette di vivere tranquillamente in giardino. Ottimo per chi adora le passeggiate in montagna.',
            born_year= 2011,
            kind= 'Incrocio da pastore',
            taglia= 'grande'
        ),
        dict(
            name= 'Luna',
            image= 'Luna_big.jpg',
            description= u'Nata nel 2007. Timida, riservata, rifugge il contatto con gli uomini, ma è perfettamente socializzata con i suoi conspecifici. E\' stata recuperata ed è quindi adottabile. Famiglia consigliata: nucleo familiare di pochi componenti, anche con bambini e con tanta pazienza per venire a conoscerla rispettando i suoi tempi.',
            born_year= 2007,
            kind= 'Meticcio',
            taglia= 'medio-piccola'
        ),
        dict(
            name= 'Leo',
            image= 'Leo_big.jpg',
            description= u'Dolcissimo e giocherellone, ha bisogno di sfogare le sue energie correndo nelle passeggiate con il suo futuro migliore amico. Può stare sia in casa che in giardino, ma se viene tenuto in casa ha bisogno di essere stimolato altrimenti se la prenderà con i mobili. Consigliato per persone dinamiche.',
            born_year= 2009,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Holly',
            image= 'Holly_big.jpg',
            description= u'Spledida esemplare, perfettamente socializzata con le persone, adatta anche ai bambini purchè non troppo piccoli perchè è un cane esuberante. Meglio se potrà essere adottata come figlia unica, senza altri cani o con un percorso di avvicinamento specifico. Non ama infatti il contatto con i suoi conspecifici. Il canile non è il posto più adatto a lei, infatti è spesso agitata.',
            born_year= 2011,
            kind= 'Amstaff',
            taglia= 'media'
        ),
        dict(
            name= 'Marton',
            image= 'Marton_big.jpg',
            description= u'Nato nel maggio 2011, attualmente in fase di recupero per via della sua timidezza. E\' pauroso ma anche molto dolce come il fratello Rodolph. Ambiente consigliato: esterno ma tranquillo preferibilmente non in città. Famiglia consigliata: Adatto a famiglie anche con bambini. L\'importante è che sia rispettato. Necessaria la preadozione.',
            born_year= 2011,
            kind= 'Incrocio nordico',
            taglia= 'grande'
        ),
        dict(
            name= 'Rodolph',
            image= 'Rodolph_big.jpg',
            description= u'Nato nel maggio 2011 è il fratello di Rodolph, attualmente in fase di recupero per via della sua timidezza. Ha un carattere indipendente. Ambiente consigliato: esterno ma tranquillo preferibilmente non in città. Famiglia consigliata: non  adatto a bambini e richiede dei compagni pazienti che rispettino i suoi tempi. Ideale la preadozione.',
            born_year= 2011,
            kind= 'Incrocio nordico',
            taglia= 'grande'
        ),
        dict(
            name= 'Birbo',
            image= 'Birbo_big.jpg',
            description= u'Dolcissimo e docilissimo adora le coccole. Vive tranquillamente sia in casa che in giardino. E\' veramente un cane adatto a tutti, anche a famiglie con bambini. D\'altra parte i suoi occhioni dolci dicono già tutto.',
            born_year= 2010,
            kind= 'Meticcio',
            taglia= 'grande'
        ),
        dict(
            name= 'Leo ',
            image= 'Leo_pb_big.jpg',
            description= u'Leo a dispetto della nomea dei pitbull è dolce ed affettuoso. Ambiente consigliato: casa, o comunque in giardino con un riparo per le giornate fredde per via del pelo raso. Adatto a persone giovani. Non deve essere adottato con l\'intento di utilizzarlo come cane da guardia. Si cede solo a persone consapevoli della razza e che lo sappiano gestire. No anziani e bambini piccoli. Adorerebbe avere una compagna in quanto si sente insicuro.',
            born_year= 2009,
            kind= 'Pitbull',
            taglia= 'medio'
        ),
        dict(
            name= 'Dora',
            image= 'Dora_big.jpg',
            description= u'Molto paurosa e diffidente. Se prende confidenza con chi la segue si trasforma in dolce ed affettuosa Ambiente consigliato: posto molto tranquillo e al calduccio, ormai gli anni si fanno sentire. Famiglia consigliata: nucleo familiare ristretto, adatta soprattutto ad anziani in quanto è un perfetto cane da compagnia. Necessita di incontri conoscitivi per via della sua diffidenza.',
            born_year= 2005,
            kind= 'Meticcio',
            taglia= 'media'
        ),
        dict(
            name= 'Norton',
            image= 'Norton_big.jpg',
            description= u'Norton è un pauroso nato, non si fida di nessuno. Uno specifico protocollo di recupero è riuscito a fortificarlo per le sue innate paure nei confronti delle persone che rimangono tuttavia molto elevate. Ambiente consigliato: appartamento in luogo tranquillo. Necessita di molti incontri conoscitivi e di molta pazienza. E\' ben accetta l\'adozione a distanza e stiamo lavorando per il recupero completo.',
            born_year= 2006,
            kind= 'Segugio',
            taglia= 'media'
        ),
        dict(
            name= 'Pippo',
            image= 'Pippo_big.jpg',
            description= u'Nato il 01/12/2007. E\' stato recupertato ed è quindi adottabile, ha davvero molto bisogno di coccole, l\'unico motivo per cui rimane in canile è la sua mole. Basta guardarlo negli occhi per capire che chiede solo un po\' di amore e pazienza. Il carattere indipendente è quello tipico del pastore dell\'Asia Centrale. Ambiente consigliato: giardino, per via della sua mole.',
            born_year= 2007,
            kind= 'Incrocio pastore Asia Centrale',
            taglia= 'gigante'
        ),
        dict(
            name= 'Ali e Saba',
            image= 'Ali_Saba_big.jpg',
            description= u'Adozione d\'amore! Hanno sempre vissuto insieme, adottati proprio dal nostro canile, molto tempo fa, sono stati da poco nuovamente ceduti. Ormai sono anziani ed necessario adottarli insieme. Sono molto timidi e necessitano di incontri conoscitivi. Sarebbero degli ottimi cani da appartamento e da compagnia per anziani.',
            born_year= 2000,
            kind= 'Husky',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Morgan',
            image= 'Morgan_big.jpg',
            description= u'',
            born_year= 2010,
            kind= 'Amsaff',
            taglia= 'medio-grande'
        ),
        dict(
            name= 'Buster',
            image= 'Buster_big.jpg',
            description= u'Splendido volpino, molto intelligente, ama i giochi di attivazione mentale, sempre disposto ad imparare cose nuove. Ottimo cane da appartamento e da compagnia. Non ama molto la manipolazione per cui ha bisogno dei suoi tempi, sarà lui a decidere quando è pronto per ricevere le coccole.',
            born_year= 2009,
            kind= 'Volpino Italiano',
            taglia= 'piccola'
        )];

        for dog in dogs:
            d = Dog(name=dog['name'], born_year=dog['born_year'],
                description=dog['description'], image=dog['image'],
                kind=dog['kind'], size=dog['taglia'])
            DBSession.add(d)

    with transaction.manager:
        events = [dict(
            title = 'Paes dei presepi',
            description = u'Abbiamo partecipato al mercatino natalizio di Baselga di Pinè; organizzato dall\'APT nel ‘Paés dei Presepi’. Gli articoli messi in vendita sono stati realizzati dai volontari del canile. Gli stessi volontari hanno messo a disposizione il proprio tempo per partecipare alla vendita degli oggetti. Abbiamo partecipato al mercatino per 3 giornate in un\'atmosfera degna del Natale. Abbiamo incontrato molte persone buone e motivate che hanno fatto un\'offerta per i nostri cagnolini. Ci siamo confrontati con i volontari di altri canili che cia hanno dato idee per nuove iniziative! Con il ricavato abbiamo comperatoe dei guinzagli e delle pettorine di cui abbiamo molto bisogno. Grazie a tutti quelli che hanno partecipato, alle persone che hanno fatto un\'offerta, e a coloro che ci hanno portato coperte, maglioni ecc...',
            date = date(2012, 12, 25)
        ),
        dict(
            title = 'Mercatino',
            description = u'Abbiamo partecipato e parteciperemo anche in futuro al mercatino dell\'usato che si tiene in centro a Rovereto tutti i primi martedì; del mese. Come per altre iniziative gli oggetti in vendita sono stati forniti o creati dagli stessi volontari che hanno poi permesso, grazie al loro tempo, di effettuare uno stand nel mercatino.',
            date = date(2013, 7, 8)
        ),
        dict(
            title = 'Incontri Scuola Cinofila Balsamo',
            description = u'Nei weekend 5-6 e 19-20 Ottobre 2013 si sono svolte presso il canile delle lezioni dal titolo \'Il cane di canile\' con la Scuola Cinofile Balsamo. Dei coinvolgentissimi incontri hai quali hanno partecipato gli alunni della Scuola Cinofila in collaborazione con i volontari e l\'associazione PAN -  EPPAA. Un ringraziamento particolare va fatto all\'insegnante Carlo Pirola della Lega del Cane di Milano e all\'educatore cinofilo Fabrizio Balsamo, titolare della scuola, i quali hanno reso possibile quest\'iniziativa che è stata molto formativa a detta di tutti i partecipanti. Speriamo in una profiqua e continua collaborazione con la scuola.',
            date = date(2013, 10, 5)
        )];

        for evt in events:
            e = Event(title=evt['title'], date=evt['date'],
                      description=evt['description'])
            DBSession.add(e)

    with transaction.manager:
        news = [dict(
            title = 'Incontri Scuola Cinofila Balsamo',
            text = u'Nei weekend 5-6 e 19-20 Ottobre 2013 si sono svolte presso il canile delle lezioni dal titolo \'Il cane di canile\' con la Scuola Cinofile Balsamo. Dei coinvolgentissimi incontri hai quali hanno partecipato gli alunni della Scuola Cinofila in collaborazione con i volontari e l\'associazione PAN -  EPPAA. Un ringraziamento particolare va fatto all\'insegnante Carlo Pirola della Lega del Cane di Milano e all\'educatore cinofilo Fabrizio Balsamo, titolare della scuola, i quali hanno reso possibile quest\'iniziativa che è stata molto formativa a detta di tutti i partecipanti. Speriamo in una profiqua e continua collaborazione con la scuola.',
            date = date(2013, 10, 5)
        )];

        for nws in news:
            e = News(title=nws['title'], date=nws['date'],
                      text=nws['text'])
            DBSession.add(e)
