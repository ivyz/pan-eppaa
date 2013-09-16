<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>The Pyramid Web Application Development Framework</title>
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
      <%header:insert_header active='about'>
      ${request}
  </%header:insert_header>
</%block>

  <div class="container">
    <img src="static/img/fiori.jpg" class="img-rounded"/>
     <div id="middle">
      <div class="middle align-center">
        <div class="span10">
          <div class="well well-large well-green margin">

      La sigla PAN-EPPAA, acronimo che sta per "Protezione Animali Natura-Ente Provinciale
      Protezione Animali e Ambiente", ne identifica efficacemente gli scopi sociali volti
      a tutelare e proteggere gli animali di ogni genere e specie, nonché il loro habitat.<br/>
      Il raggiungimento di questo scopo avviene attraverso la realizzazione e la gestione,
      anche per conto di terzi, di strutture atte al temporaneo ricovero di animali bisognosi
      di custodia o di cura, l'attività di sensibilizzazione ed educazione alle tematiche
      animaliste e ambientalistiche anche in collaborazione con ogni altra Associazione avente
      scopi uguali o affini, la cooperazione o la sollecitazione delle autorità competenti
      affinché siano osservate o poste in atto le norme nazionali e provinciali in materia di
      protezione degli animali e dell'ambiente.<br/>
      La PAN-EPPAA gestisce direttamente le maggiori strutture di accoglienza per animali
      randagi o in difficoltà della Provincia di Trento.
      <br/><br/>
      La cultura animalista ha a cuore tutti gli animali.<br/>
      In 25 anni abbiamo raccolto numerosi soggetti selvatici feriti o in difficoltà (ungulati,
      uccelli, rettili), riuscendo il più delle volte a rimetterli in libertà dopo averli sottoposti
      a cure veterinarie specialistiche. Interveniamo nel caso di segnalazioni di maltrattamenti
      di animali domestici tramite il nostro Nucleo di Polizia Zoofila che, nello specifico,
      svolge funzioni di Polizia Giudiziaria, in base alla legge n.189 del 20 luglio 2004
      presentando denunce alla Magistratura, unitamente alle Guardie Faunistiche Volontarie,
      le quali si occupano di materia venatoria ed è diventata punto di riferimento per i cittadini
      del Trentino, e anche per la pubblica Amministrazione in materia di problemi giuridici che
      riguardano gli animali. <br/><br/>
      Per svolgere un'attività a tutto campo servirebbero molte forze, animate da disponibilità
      e competenza in fatto di leggi e regolamenti. Ma nella nostra provincia il nucleo di
      Guardie Zoofile è limitato a pochi elementi e delle Guardie Faunistiche che inizialmente
      erano tre, ne è rimasta una sola per tutto il territorio.
      Un’altra mancanza grave, che pesa notevolmente nell’azione preventiva e repressiva è la
      mancata approvazione di una legge provinciale articolata ed esaustiva per la protezione
      degli animali.<br/>
      L’approvazione di un Regolamento da parte della Giunta Provinciale, concernente l’Anagrafe
      canina provinciale ed i canili, tra l’altro inapplicata, non è riuscita a migliorare di
      molto la situazione.
<br/><br/>
        La PAN - E.P.P.A.A. è una ONLUS che si finanzia quasi esclusivamente con le donazioni e
        le iscrizioni
        sede legale: 38068 Rovereto, via Balteri, 2
        Codice Fiscale - Partita I.V.A. 01142600228
        Banca d'appoggio: Rurale Giudicarie Valsabbia Paganella C.C. 10/1001136 ABI 08078 CAB 35540
        Conto corrente Postale n° 11244381

        Canile di Rovereto: Tel: 339 4141717 - Via delle Zigherane, Loc. Ai Fiori, Rovereto 38068

        Gattile di Trento: Tel: 0461 232810 - via S.Martino, 23 38100 Trento

        Gattile di Riva del Garda: Tel: 0464 522171 – viale dei Tigli, 47/d - 38066 Riva del Garda

        per informazioni: info@protezioneanimali.tn.it
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
