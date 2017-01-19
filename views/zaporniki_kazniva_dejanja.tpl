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
     <a href ="http://127.0.0.1:8080/zaporniki/kazniva_dejanja/" class="black-text collection-item active"> Kazniva dejanja zapornika </a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/finance/" class="black-text collection-item"> Finance zapornika</a> 
     <a href ="http://127.0.0.1:8080/zaporniki/delo/" class="black-text collection-item"> Delo zapornika </a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj/" class="black-text collection-item "> Dodaj zapornika</a>
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj_kazen/" class="black-text collection-item"> Dodaj kazen</a> 	 
 </div>
 </div>
 <div class = "col s8">
  <p>Poišči vse kazni zapornika z danim id-jem. V primeru, da želiš izvedeti več o posamezni kazni, pojdi na stran o kaznih in vtipkaj id izbrane kazni.</p>
  <br>
  <form action = "/zaporniki/kazniva_dejanja/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
  <br>
  <br>
  <br>
%if kazni == None:
	%if vnos!="":
		<p> Zapornik z id-jem <b>{{vnos}}</b> ne obstaja. </p>
	%end
%else:
    <table>
        <thead>
          <tr>
              <th>Id kazni</th>
              <th>Vrsta zločina</th>
              <th>Datum prihoda</th>
			  <th>Datum odhoda</th>
          </tr>
        </thead>
		<tbody>
		%for kazen in kazni.values():
			%id_kazni = kazen[0]
			%vrsta_kazni = kazen[1]
			%zacetek = kazen[2]
			%konec = kazen[3]
			<tr>
				<td>{{id_kazni}}</td>
				<td>{{vrsta_kazni}}</td>
				<td>{{zacetek}}</td>
				<td>{{konec}}</td>
            </tr>
		%end
		</tbody>
	</table>		
%end
 </div>
</div>