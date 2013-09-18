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
      <%header:insert_header active='help'>
      ${request}
  </%header:insert_header>
</%block>

  <div class="container">
    <img src="static/img/fiori.jpg" class="img-rounded span12" id="topimg"/>
    <div id="middle">
      <div class="middle align-center">
      <div class="span12">
        <div class="well well-large well-green margin">
          <h5>
            In occasione della prossima denuncia dei redditi, scegliete
            di assegnare il 5 per mille a Pan - Eppaa onlus - Rovereto -
            partita I.V.A. 01142600228. Vi ringraziamo anticipatamente.
          </h5>
        </div>
        <h2>Di cosa abbiamo bisogno:</h2>
        <ul class="unstyled">
          <li>
            <dl class="dl-horizontal">
              <dt>Coperte</dt>
              <dd>L'inverno fa freddo, ed alcuni cani sono molto
                anziani. Portaci le coperte che no usi più, lenzuola,
                tappeti... possibilemente puliti. Li usiamo anche per
                i cani operati che necessitano di pulizia assoluta.</dd><br/>
              <dt>Cibo</dt>
              <dd>Pane, bocconcini, croccantini, riso soffiato!
                I cani vengono educati con la filosofia del premio
                quindi servono anche biscottini!</dd><br/>
              <dt>Maglioni / capottini</dt>
              <dd>Se volete potete portarci dei cappottini o anche
                semplicemente dei maglioni che non usate più dai
                quali ricaveremo noi dei cappottini! Vanno bene anche
                dei calzini di lana per i cagnolini più piccoli.</dd><br/>
              <dt>Guinzagli e pettorine</dt>
              <dd>I nostri guinzagli vengono usati tantissimo e
                spesso si rompono quindi ne abbiamo sempre bisogno
                (possibilmente fissi). </dd><br/>
                <dt>Cuccie e casette</dt>
                <dd>Quelle che abbiamo sono molto usurate.</dd><br/>
                <dt>Acessori</dt>
                <dd>Servono anche spazzole,
                pettini e accessori simili, collari e pettorine.</dd><br/>
              <dt>Giochi</dt>
              <dd>E' importante per i cani agitati sfogare la
                propria energia, ed il metodo migliore è il gioco. </dd>
            </dl>
          </li>
        </ul>
      </div>

      </div>
    </div>
  </div>
      <%block name="footer_bar">
      <%footer:insert_footer></%footer:insert_footer>
  </%block>
</body>
</html>
