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
  <div class="container">
    <%block name="header_bar">
      <%header:insert_header active='news'>
      ${request}
    </%header:insert_header>
    </%block>

    <img src="static/img/news.jpg" class="img-rounded" id="topimg"/>
        <div class="container-fluid">
        <h1>News</h1>

        % for d in news:
        <div class="row">
          <div class="span8">
            <!--a href="${request.route_url('events')}/${d.id}"><h3>${d.title}</h3></a-->
            <h3>${d.title}</h3>
          </div>
          <div class="span4 date">Quando: ${d.date}</div>
        </div>
        <div class="row">
          <div class="span3">
            <img src="${d.image}" class="img-rounded"/>
          </div>
          <div class="span9">
            <br/>${d.text}
          </div>
          % if d.video:
             <div class="span3">
               <video width="320" height="240" controls>
                 <source src="${d.video}" type="video/mp4"/>
               </video>
             </div>
          % endif
        </div>
        %endfor
      </div>
    </div>
  <%block name="footer_bar">
      <%footer:insert_footer></%footer:insert_footer>
  </%block>

</body>
</html>
