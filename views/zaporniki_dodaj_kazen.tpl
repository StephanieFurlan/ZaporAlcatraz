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
     <a href ="http://127.0.0.1:8080/zaporniki/delo/" class="black-text collection-item"> Delo zapornika </a> 	 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj/" class="black-text collection-item"> Dodaj zapornika</a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj_kazen/" class="black-text collection-item active"> Dodaj kazen</a> 
 </div>
 </div>
 <div class = "col s8">
	<br>
	<form action="/zaporniki/dodaj_kazen/" method = "post">
		<div class="input-field">
			<input type = "text" name = "id_zapornika">
			<label for="first_name">Id zapornika</label>
		</div>
		<div class="input-field">
			<input name="trajanje" type="text" id = "trajanje">
			<label for="ime">Trajanje</label>
		</div>
		<div class="input-field">
			<input name="denarna_kazen" type="text" id ="denarna_kazen">
			<label for="denarna_kazen">Denarna kazen</label>
		</div>
		<div class="input-field">
			<select name ="vrsta_zlocina" id ="vrsta_zlocina" type = "text" >
				<option value="" disabled selected>Vrsta zločina</option>
				<option value="davcna utaja">Davčna utaja</option>
				<option value="terorizem">Terorizem</option>
				<option value="kraja">Kraja</option>
				<option value="mucenje zivali">Mučenje živali</option>
				<option value="nenaklepni umor">Nenaklepni umor</option>
				<option value="naklepni umor">Naklepni umor</option>
				<option value="pedofilija">Pedofilija</option>
				<option value="posilstvo">Posilstvo</option>
				<option value="pranje denarja">Pranje denarja</option>
				<option value="razpecevanje droge">Razpečevanje droge</option>
			</select>
			<label>Vrsta zločina</label>
		</div>
			<br>
			<label>Možnost pomilostitve: </label>
			<p>
			  <input class="with-gap" name="pomilostitev" type="radio" id="JA" value="JA" />
			  <label for="JA">Da</label>
			</p>
			<p>
			  <input class="with-gap" name="pomilostitev" type="radio" id="NE" value="NE" />
			  <label for="NE">Ne</label>
			</p>
		<br>
		<br>
		<button class="btn waves-effect waves-light" type = "submit" > Dodaj </button>
	</form>
</div>
</div>