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
      <%header:insert_header active='events'>
      ${request}
  </%header:insert_header>
</%block>

  <div id="wrap">
    <div id="top">
      <div class="top align-center">
        <div><img src="${request.static_url('paneppaa:static/pyramid.png')}" width="750" height="169" alt="pyramid"/></div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-center">
        <p class="app-welcome">
          <span class="app-name">${event.title}</span>
        </p>
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
            <b><span>${event.title}</span></b><br/>
            <span>${event.description}</span><br/>
            <span>Quando: ${event.date}</span><br/><br/>
      </div>
    </div>
  </div>
      <%block name="footer_bar">
      <%footer:insert_footer show_lang="0"></%footer:insert_footer>
  </%block>
</body>
</html>
