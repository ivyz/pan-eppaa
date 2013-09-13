<%def name="insert_header(product='paneppaa', active='dogs')">
<div class="navbar navbar-inverse navbar-fixed-top" id="header">
  <div class="navbar-inner">
    <div class="container">
      <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </a>
      <a class="brand" href="index.php">PAN EPPAA</a>
      <div class="nav-collapse collapse">
        <img src="${request.static_url('paneppaa:static/img/logo.png')}" width='60px' height='60px'/>
        <ul class="nav">
          % if active == 'dogs':
            <li class="active">
          %else:
            <li>
          %endif
          <a href="${request.route_url('dogs')}">I nostri cani</a>
          </li>
          <!--li>
            <a href="adopted.php" class="big">Adottati</a>
          </li-->
          <li>
          <a href="${request.route_url('about')}">Su di noi</a>
          </li>
          % if active == 'events':
            <li class="active">
          %else:
            <li>
          %endif
          <a href="${request.route_url('events')}">Eventi</a>
          </li>
          <li>
          <a href="${request.route_url('advice')}">Consigli</a>
          </li>
          <!--li>
            <a href="contact.php" class="big">Contatti</a>
          </li-->

          <li>
          <a href="${request.route_url('help')}">Aiutaci</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
</%def>
