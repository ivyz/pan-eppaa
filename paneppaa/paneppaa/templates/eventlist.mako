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
      <%header:insert_header active='events'>
      ${request}
      </%header:insert_header>
      </%block>
      <img src="static/img/events.jpg" class="img-rounded span12" id="topimg"/>
        <div class="container-fluid">
        <h1>Eventi</h1>

        % for d in events:
        <div class="row">
          <div class="span7">
            <a href="${request.route_url('events')}/${d.id}"><h3>${d.title}</h3></a>
          </div>
          <div class="span4 date">Quando: ${d.date}</div>
        </div>
        <div class="row">
          <div class="span3">
            <img src="img/mercatino1.jpg" class="img-rounded"/>
          </div>
          <div class="span7">
            <br/>Descrizione: ${d.description}
          </div>
        </div>
        %endfor
      </div>
    </div>
    <%block name="footer_bar">
    <%footer:insert_footer></%footer:insert_footer>
    </%block>
  </body>
</html>
