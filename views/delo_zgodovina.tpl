%rebase('osnova.tpl')
<div class = "row">
	<nav>
		<div class = "nav-wrapper teal lighten-1">
			<ul class= "hide-on-med-and-down right">
				<li><a href ="http://127.0.0.1:8080/" class ="white-text"><i class = "material-icons">home</i> </a></li>
			</ul>  
		</div>
	</nav>
 <div class="col s4">
	 <div class = "collection">
		<a href ="http://127.0.0.1:8080/delo/prosto/" class="black-text collection-item"> Prosta dela </a></li>
		<a href ="http://127.0.0.1:8080/delo/zgodovina/" class="black-text collection-item active"> Zgodovina dela  </a> </li>
	 </div>
 </div >
 <div class = "col s8">
	<br>
	Poiščite vse delavne aktivnosti v zaporu v naslednjem časovnem intervalu:
	<br>
	<br>
 	<form action = "/delo/zgodovina/" method = "get">
		<div class = "col s6">
			<label>Začetek</label>              
			<input type="date" name = "zacetek" id = "zacetek" class="datepicker">
		</div> 
		<div class = "col s6">
			<label>Konec</label>              
			<input type="date" name = "konec" id = "konec" class="datepicker">
		</div>
		<button class="btn waves-effect waves-light" type = "submit" > Poišči </button>
	</form>
	<br>
	<br>
	<br>
	%if zgodovina != None:
		<table>
        <thead>
          <tr>
              <th>Datum</th>
              <th>Id zapornika</th>
              <th>Vrsta dela</th>
			  <th>Število ur</th>
			  <th>Zaslužek</th>
          </tr>
        </thead>
		<tbody>
		%for (datum, delavec, delo, st_ur, zasluzek) in zgodovina:
			<tr>
				<td>{{datum}}</td>
				<td>{{delavec}}</td>
				<td>{{delo}}</td>
				<td>{{st_ur}}</td>
				<td>{{zasluzek}}</td>
            </tr>
		%end
		</tbody>
		</table>
	%end
 </div>
 </div>
