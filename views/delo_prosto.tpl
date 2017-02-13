%rebase('osnova.tpl')
<div class = "row">
 <nav>
  <div class = "nav-wrapper teal lighten-1">
   <ul class= "hide-on-med-and-down right">
    <li><a href ="http://127.0.0.1:8080/" class ="white-text"><i class = "material-icons">home</i> </a></li>
   </ul>  
  </div>
 </nav>
 <div class = "col s4 collection">
     <a href ="http://127.0.0.1:8080/delo/prosto/" class="black-text collection-item active"> Prosta dela  </a> </li>
	 <a href ="http://127.0.0.1:8080/delo/zgodovina/" class="black-text collection-item"> Zgodovina dela  </a> </li>
 </div>
<div class = "col s8">
	<br>
	Na tej strani lahko najdete vse podatke o prostih delavnih mestih v zaporu. Ker je število delavnih mest v zaporu omejeno vodimo evidenco o prostih delavnih mestih. Vsa trenutno prosta dela so zapisana v spodnji tabeli:
    <br>
	<br>
	<table>
        <thead>
          <tr>
              <th>Vrsta dela</th>
              <th>Število prostih mest</th>
			  <th>Urna postavka</th>
          </tr>
        </thead>
		<tbody>
		%for (delo, st) in zip(vsa_prosta.keys(), vsa_prosta.values()):
			<tr>
				<td>{{delo}}</td>
				<td>{{st}}</td>
				<td>{{urne_postavke[delo]}}</td>
            </tr>
		%end
		</tbody>
	</table>
	<br>
	<br>
	<br>
	<br>
	V primeru, da želi zapornik plačati manj denarne kazni, potem lahko v zaporu dela.
	<br>
	<form action = "/delo/prosto/" method = "post">
		<div class="input-field">
			<input name="id_zapornika" type="text" id ="id_zapornika">
			<label for="id_zapornika">Id zapornika</label>
		</div>
		<div class="input-field">
			<select name ="delo" id ="delo" type = "text" >
				<option value="" disabled selected>Vrsta dela</option>
				%slovarDel = {"kuhar" :"Kuhar/ica", "pleskar" :"Pleskar/ka" , "cistilec" : "Čistilec/ka", "knjiznicar" : "Knjižničar/ka", "mizar" :"Mizar/ka", "vrtnar" : "Vrtnar/ka", "pralec" : "Pralec/ka"}
			%for (delo, st) in zip(vsa_prosta.keys(), vsa_prosta.values()):
				<option value="{{delo}}">{{slovarDel[delo]}}</option>
			%end
			</select>
			<label>Vrsta dela</label>
		</div>
		<div class="input-field">
			<input name="st_ur" type="text" id ="st_ur">
			<label for="st_ur">Število ur</label>
		</div>
		<button class="btn waves-effect waves-light" type = "submit" > Dodaj </button>
	</form>
</div>	
