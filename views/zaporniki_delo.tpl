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
     <a href ="http://127.0.0.1:8080/zaporniki/poisci/" class="black-text collection-item"> Poišči zapornika </a> 
     <a href ="http://127.0.0.1:8080/zaporniki/kazniva_dejanja/" class="black-text collection-item "> Kazniva dejanja zapornika </a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/finance/" class="black-text collection-item"> Finance zapornika</a> 
     <a href ="http://127.0.0.1:8080/zaporniki/delo/" class="black-text collection-item active"> Delo zapornika </a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj/" class="black-text collection-item"> Dodaj zapornika</a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj_kazen/" class="black-text collection-item "> Dodaj kazen</a> 
 </div>
 </div>
 <div class = "col s8">
   <p>Zgodovina dela v zaporu za posameznega zapornika.</p>
  <br>
  <form action = "/zaporniki/delo/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
    <br>
  <br>
  <br>
%if delo == None:
	%if vnos!="":
		<p> Zapornik z id-jem <b>{{vnos}}</b> ne obstaja. </p>
	%end
%else:
    <table>
        <thead>
          <tr>
              <th>Id delo</th>
              <th>Datum</th>
              <th>Vrsta dela</th>
			  <th>Število ur</th>
			  <th>Zaslužek</th>
          </tr>
        </thead>
		<tbody>
		
		%for (id_delo, datum, vrsta, st, zasluzek) in delo[0] + delo[1]:
			<tr>
				<td>{{id_delo}}</td>
				<td>{{datum}}</td>
				<td>{{vrsta}}</td>
				<td>{{st}}</td>
				<td>{{zasluzek}}</td>
            </tr>
		%end
		</tbody>
	</table>		
%end
 </div>
</div>
