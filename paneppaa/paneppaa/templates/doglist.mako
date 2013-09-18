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
    <div class="container">

    <%block name="header_bar">
      <%header:insert_header active='dogs'>
      ${request}
      </%header:insert_header>
    </%block>

      <section id="carousel">
        <div class="bs-docs-example">
          <div id="myCarousel" class="carousel slide">
            <div class="carousel-inner img-rounded">
              <div class="item active">
                <img src="${request.static_url('paneppaa:static/img/header1.jpg')}" alt=""/>
                <div class="carousel-caption">
                  <h4>A spasso e coccole</h4>
                  <p>Stuard e Poldo vanno a spasso, mentre Diana si
                    prende un mare di coccole!</p>
                </div>
              </div>
              <div class="item">
                <img src="${request.static_url('paneppaa:static/img/sfondo2.jpg')}" alt=""/>
                <div class="carousel-caption">
                  <h4>Foto d'autore</h4>
                  <p>Alcuni primi piani ben riusciti</p>
                </div>
              </div>
            </div>
            <a class="left carousel-control" href="#myCarousel" data-slide="prev">&lsaquo;</a>
            <a class="right carousel-control" href="#myCarousel" data-slide="next">&rsaquo;</a>
          </div>
        </div>
      </section>

      <%def name="truncateDescription(descr)">
      <%
         return descr[:105] + '...'
      %>
      </%def>

      <div class="row">
        % for d in dogs:
        <div class="span4 well">
          <h2>${d.name}</h2>
          <img src="${request.static_url('paneppaa:static/img')}/${d.image}" class="img-rounded"/>
          <p class="margin">${truncateDescription(d.description)}
          </p>
          <p>
            <a class="btn btn-success" href="${request.route_url('dogs')}/${d.id}">Conoscimi  &raquo;</a>
          </p>
        </div>
        % endfor
      </div>
      </div>

   <%block name="footer_bar">
      <%footer:insert_footer></%footer:insert_footer>
   </%block>

  </body>
</html>
