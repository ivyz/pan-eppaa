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
    <script>
    //var staticurl = ${request.static_url('paneppaa:static/img')};
    function changeImage(n)	{
         alert(n);
        document.getElementById('bigimage').src = staticurl;/* + '/'+ ${dog.name} + n + 'jpg';*/
    }
    </script>
</head>

<body>
  <%block name="header_bar">
    <%header:insert_header active='dogs'>
    ${request}
    </%header:insert_header>
  </%block>


  <div class="container">
    <h1 class="title">${dog.name}</h1>
    <img id="bigimage" src="${request.static_url('paneppaa:static/img')}/${dog.name}1.jpg"
         height="270" width="360" alt="camera"  class="img-rounded"/>
    <img src="${request.static_url('paneppaa:static/img')}/${dog.name}1.jpg"
         height="90" width="120"  class="img-rounded"
         alt="camera" onclick="changeImage(1)"/>
    <img src="${request.static_url('paneppaa:static/img')}/${dog.name}2.jpg"
         height="90" width="120" class="img-rounded"
         alt="camera" onclick="changeImage(2)"/>
    <img src="${request.static_url('paneppaa:static/img')}/${dog.name}3.jpg"
         height="90" width="120" class="img-rounded"
         alt="camera" onclick="$('#bigimage').attr('src', $(event.target).attr('3.jpg'))"/>
    <hr>
      <span>Razza: ${dog.kind}</span><br/>
      <span>Taglia: ${dog.size}</span><br/><br/>
      <div>${dog.description}</div><br/>
      </div>
    </div>
  </div>

  <%block name="footer_bar">
    <%footer:insert_footer></%footer:insert_footer>
  </%block>

  </body>
</html>
