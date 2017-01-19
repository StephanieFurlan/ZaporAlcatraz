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
	 <a href ="http://127.0.0.1:8080/zaporniki/finance/" class="black-text collection-item active"> Finance zapornika</a> 
     <a href ="http://127.0.0.1:8080/zaporniki/delo/" class="black-text collection-item"> Delo zapornika </a> 	 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj/" class="black-text collection-item"> Dodaj zapornika</a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj_kazen/" class="black-text collection-item "> Dodaj kazen</a> 
 </div>
 </div>
 <div class = "col s8">
   <p>Finance posameznega zapornika.</p>
  <br>
  <form action = "/zaporniki/finance/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
%if delo == None:
	%if vnos!="":
		<p> Zapornik z id-jem <b>{{vnos}}</b> ne obstaja. </p>
	%end
%else:
	% pred = delo[0]
	% zasluzekPred = zasluzek[0]
	% po = delo[1]
	%zasluzekPo = zasluzek[1]
	% if len(pred) != 0:
		<br>
		Finance pred zadnjo aretacijo:
		<table>
			<thead>
			  <tr>
				  <th>Id dela</th>
				  <th>Datum</th>
				  <th>Zaslužek</th>
				  <th>Dolžen</th>
			  </tr>
			</thead>
			<tbody>
			%for (id_dela, datum, vrsta_dela, st_ur, zasluzek) in pred:
				<tr>
					<td>{{id_dela}}</td>
					<td>{{datum}}</td>
					<td>{{zasluzek}}</td>
					<td></td>
					
				</tr>
			%end
				<tr>
					<td></td>
					<td></td>
					<td><b>{{zasluzekPred}}</b></td>
					<td><b>{{dolzanPred}}</b></td>
					
				</tr>
			</tbody>
		</table>
	%end
	
	<br>
	Finance trenutne aretacije:
	<table>
		<thead>
		  <tr>
			  <th>Id dela</th>
			  <th>Datum</th>
			  <th>Zaslužek</th>
			  <th>Dolžen</th>				 
		  </tr>
		</thead>
		<tbody>
		%for (id_dela, datum, vrsta_dela, st_ur, zasluzek) in po:
			<tr>
				<td>{{id_dela}}</td>
				<td>{{datum}}</td>
				<td>{{zasluzek}}</td>
				<td></td>
				
			</tr>
		%end
			<tr>
				<td></td>
				<td></td>
				<td><b>{{zasluzekPo}}</b></td>
				<td><b>{{dolzanPo}}</b></td>
				
			</tr>
		</tbody>
	</table>
%end
 </div>
</div>
