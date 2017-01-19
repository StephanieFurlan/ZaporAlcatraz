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
     <a href ="http://127.0.0.1:8080/celice/poisci/" class="black-text collection-item active"> Sojetniki </a> 	
     <a href ="http://127.0.0.1:8080/celice/proste/" class="black-text collection-item "> Proste celice </a> 	
     <a href ="http://127.0.0.1:8080/celice/zamenjaj/" class="black-text collection-item"> Zamenjaj celice </a> 		 
 </div>
 </div>
 <div class = "col s8">
  <p>Poišči sojetnike v celici.</p>
  <br>
  <form action = "/celice/poisci/">
   <div class="input-field">
    <input type = "text" name = "st_celice">
    <label for="st_celice">Številka celice</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
  <br>
  <br>
  <br>
%if zaporniki == None:
	%if vnos!="":
		<p> Celica z id-jem <b>{{vnos}}</b> ne obstaja. </p>
	%end
%else:
    <table>
        <thead>
          <tr>
              <th>Datum</th>
              <th>Id zapornika</th>
              <th>Ime</th>
			  <th>Priimek</th>
          </tr>
        </thead>
		<tbody>
		%for (datum, id_zapornika, ime, priimek) in zaporniki:
			<tr>
				<td>{{datum}}</td>
				<td>{{id_zapornika}}</td>
				<td>{{ime}}</td>
				<td>{{priimek}}</td>
            </tr>
		%end
		</tbody>
	</table>		
%end
 </div>
</div>