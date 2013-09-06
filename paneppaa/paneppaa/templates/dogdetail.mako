<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>The Pyramid Web Application Development Framework</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />
  <link rel="shortcut icon" href="${request.static_url('paneppaa:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('paneppaa:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/nobile/stylesheet.css" media="screen" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/neuton/stylesheet.css" media="screen" />
  <!--[if lte IE 6]>
  <link rel="stylesheet" href="${request.static_url('paneppaa:static/ie6.css')}" type="text/css" media="screen" charset="utf-8" />
  <![endif]-->
</head>
<body>
  <div id="wrap">
    <div id="top">
      <div class="top align-center">
        <div><img src="${request.static_url('paneppaa:static/pyramid.png')}" width="750" height="169" alt="pyramid"/></div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-center">
        <p class="app-welcome">
          <span class="app-name">${dog.name}</span>
        </p>
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
            <span>Nome: ${dog.name}</span><br/>
            <span>Descrizione: ${dog.description}</span><br/>
            <span>Razza: ${dog.kind}</span><br/>
            <span>Taglia: ${dog.size}</span><br/><br/>

      </div>
    </div>
  </div>
  <div id="footer">
    <div class="footer">&copy; Copyright 2013 silvia.zobele@gmail.com</div>
  </div>
</body>
</html>
