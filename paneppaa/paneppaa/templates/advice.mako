<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
  <head>
    <title>Canile PAN EPPAA - Rovereto</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
    <meta name="keywords" content="python web application" />
    <meta name="description" content="pyramid web application" />
    <link href="${request.static_url('paneppaa:static/css/bootstrap.css')}" rel="stylesheet"/>
    <link href="${request.static_url('paneppaa:static/css/custom-style.css')}" rel="stylesheet"/>
    <link href="${request.static_url('paneppaa:static/css/bootstrap-responsive.css')}" rel="stylesheet"/>
    <link href="${request.static_url('paneppaa:static/css/bootstrap.min.css')}" rel="stylesheet"/>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="${request.static_url('paneppaa:static/js/bootstrap.min.js')}"></script>
    <%namespace file="footer.mako" name="footer"/>
    <%namespace file="header.mako" name="header"/>
  </head>

  <body>
    <%block name="header_bar">
    <%header:insert_header active='advice'>
    ${request}
  </%header:insert_header>
</%block>

<div class="container">
  <img src="static/img/fiori.jpg" class="img-rounded" id="topimg"/>
  <div id="middle">
    <div class="middle align-center">
      <div>
        <div class="well well-large well-green margin">

          <b><h3>CONSIGLI PER I NUOVI PROPRIETARI</h3></b><br/>
          <div>
            Queste poche righe sono state scritte con l'intento di far si che i nuovi proprietari
            possano passare una vita il più possibile serena con il loro nuovo amico peloso.
          </div><br/>
          <div>
            Abbiamo scritto questi consigli in base alle nostre esperienze (senza pretese di
            completezza o competenze da navigati educatori cinofili). Sappiamo infatti che a volte
            capirsi tra specie diverse può essere difficile, e sicuramente non immediato.<br/>
            Il cane comunica in modo diverso da noi, la maggior parte dei cani si adegua ai nostri
            “strani” modi, ma alcuni potrebbero non capirvi immediatamente.
          </div><br/>
          <div>
            Ricordati che per il momento tu non sei il suo “adorato padroncino” ma solo un umano
            che lo porta in un ambiente nuovo, che può essere certamente più piacevole del canile,
            ma il cane non lo sa ancora.
          </div><br/>
          <div>
            Parti dal presupposto che per lui è tutto nuovo.<br/>
            Il tuo nuovo amico potrebbe non sapere che non si può salire sul divano, se vuoi farlo
            scendere non tiralo, lui non sa che lo fai solo per proteggere il nuovissimo
            rivestimento! <br/>
            Prendi invece un invitante bocconcino e chiamalo a te, poi fallo andare nella sua
            cuccia e premialo nuovamente.<br/>
            Il modo migliore è la prevenzione, copri il divano o rendilo inagibile fino a che il
            tuo amico non ha capito che il suo posto è la cuccia.
          </div><br/>
          <div>
            Abbi pazienza se sporca in casa, in genere ogni cane preferisce sporcare all'esterno,
            ma deve prendere i tuoi ritmi, vedrai che una volta abituato non ci saranno problemi.<br/>
            Non pretendere che il primo giorno si lasci prendere in braccio o pulire le zampette al
            ritorno da una passeggiata. (I cani non amano essere toccati sulle zampe né farsi mettere
            una mano in testa dall'ultimo arrivato).
          </div><br/>x
          <div>
            Non portarlo dal veterinario, alla toelettatura, all'area cani, a conoscere tutti i tuoi
            amici e parenti il primo giorno...
          </div><br/>
          <div>
            Guadagnati la sua fiducia, come? Con dei giochi, ma anche insegnandogli cose nuove!
            I cani adorano imparare! Hanno bisogno che tu sia la loro guida!
          </div><br/>
          <div>
            Non riportarlo al canile solo perché le cose non vanno subito come pensavi, ogni cane,
            specialmente se preso in un canile ha delle esperienze alle spalle che potrebbero non
            essere state piacevoli.<br/>
            Ha bisogno di tempo per fidarsi di te (o di voi).
          </div><br/>
          <br/>
          <div>
            <b><h4>GIOCHI:</h4></b>
          </div><br/>
          <div>
            Il miglior modo di insegnare qualcosa al cane è tramite il gioco. I giochi che
            coinvolgono l'olfatto sono i migliori per i cani che hanno bisogno di sfogare le proprie
            energie perché una consistente parte del cervello del cane è adibita all'olfatto.<br/>
            Ecco alcuni giochi che ti aiuteranno a guadagnarti la fiducia del tuo nuovo amico.
          </div><br/>
          <div>
            <ol>
              <li>
                Occorrente: vasetti dello yogurt vuoti o confezioni di cartone, premi<br>
                  Nascondi i premi sotto alcuni dei vasetti e incita il tua amico a cercarli!
                  Appena mette il naso a terra digli ‘Bravo!’ così capisce che è proprio ciò che vuoi!
                </li>
              <li>
                Occorrente: asciugamano, premi<br/>
                Arrotola alcuni premi in un vecchio asciugamano, il tuo amico dovrà srotolarlo
                per trovarli.
              </li>
              <li>
                Occorrente: pazienza :) <br/>
                Insegna alcuni comandi al cane (il seduto in genere lo fanno già tutti i nostri cani)
                come ad esempio TERRA, RESTA, CERCA.<br/>
                <b>Terra:</b> fagli assumere la posizione da seduto, poi con un bocconcino in mano fai
                passare la mano davanti al muso e giù perpendicolare al terreno fino a terra, poi
                parallelamente al terreno in avanti;<br/>
                <b>Resta:</b> con un bocconcino dietro la schiena dai il segno di “alt” con l'altra
                mano e indietreggia di qualche passo per poi tornare da lui, se è rimasto li seduto
                premialo, aumenta gradualmente il numero di passi;<br/>
                <b>Cerca:</b> nascondi dei bocconcini come spiegato in 1) e incita il tuo amico a cercare,
                appena inizia ad annusare digli “Bravo”.
                E' un gioco che puoi fare anche mentre state andando in passeggiata, senza farti vedere,
                butta qualche bocconcino a terra e incita il cane con un bel “cerca, cerca!”<br/>
                Renderà la passeggiata un momento di collaborazione.
              </li>
              </ol>
            </div>
            <div>
              Evitate si far giocare il cane con le scarpe, lui non distingue quelle nuove che avete
              acquistato per il matrimonio del prossimo week-end da quelle vecchie e spaiate.</br>
            Il cane deve riuscire a “vincere”, non fate giochi in cui il cane non arriverà mai al
            premio altrimenti perderà interesse.
          </div>
          <div>
            Quando andate al lavoro e il cane rimane da solo potete spargere in giardino (o in case
            se rimane in casa) dei bocconcini nascosti. Si annoierà di meno attendendo il vostro arrivo.<br/>
            Può essere utile anche l'uso di alcuni busy toys come il Kong.
          </div>
          <div>
            Ricordatevi che per l'obbedienza i comandi devono essere comprensibili, brevi e ben marcati
            (SEDUTO, TERRA, NO), ma per i complimenti al vostro amico potete tranquillamente dilungarvi
            in smancerie a piacere :)
          </div>
          <div>
            Se hai dei dubbi o ti trovi in difficoltà, o vuoi semplicemente approfondire l'argomento non
            esitare a contattarci.
          </div>
          <div>
            Ci trovi su facebook: “Canile Rovereto”<br/>
            e Gmail: canilerovereto@gmail.com<br/>
          </div>
          <div>
            Ti consigliamo, se hai voglia di informarti, dei siti simpatici e interessanti:<br/>
            www.tipresentoilcane.com<br/>
            www.petsandthecity.it<br/>
          </div>

        </div>
      </div>
    </div>
  </div>
  </div>
  <%block name="footer_bar">
  <%footer:insert_footer></%footer:insert_footer>
</%block>

</body>
</html>
