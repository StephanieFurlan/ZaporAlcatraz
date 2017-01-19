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
     <a href ="http://127.0.0.1:8080/zaporniki/poisci/" class="black-text collection-item active"> Poišči zapornika </a> 
     <a href ="http://127.0.0.1:8080/zaporniki/kazniva_dejanja/" class="black-text collection-item "> Kazniva dejanja zapornika </a>
	 <a href ="http://127.0.0.1:8080/zaporniki/finance/" class="black-text collection-item"> Finance zapornika</a> 
     <a href ="http://127.0.0.1:8080/zaporniki/delo/" class="black-text collection-item"> Delo zapornika </a> 	 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj/" class="black-text collection-item "> Dodaj zapornika </a> 
	 <a href ="http://127.0.0.1:8080/zaporniki/dodaj_kazen/" class="black-text collection-item"> Dodaj kazen</a> 
 </div>
 </div>
 <div class = "col s8">
 	<br>
	%if ime == None:
		%if vnos!="":
			<p> Zapornik z id-jem <b>{{vnos}}</b> ne obstaja. </p>
		%end
	%else:
	   <ul class="collection">
		 <li class="collection-item"><big><b>Ime:   </b>{{ime}}</big></li>
		 <li class="collection-item"><big><b>Priimek:   </b>{{priimek}}</big></li>
		 <li class="collection-item"><big><b>Datum rojstva:   </b>{{datum_rojstva}}</big></li>
		 <li class="collection-item"><big><b>Spol:   </b>{{spol}}</big></li>
		 <li class="collection-item"><big><b>Celica:   </b>{{celica}}</big></li>
	   </ul>
	    <br>
		<br>
		<br>
	%end
  <br>
  <form action = "/zaporniki/poisci/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
  <br>
  <br>
  <br>
  <p>Poišči vse zapornike po imenu, priimku, dtumu rojstva, spolu.</p>
  <form action="/zaporniki/poisciVsi/" >
		<div class="input-field">
			<input name="ime" type="text">
			<label for="ime">Ime</label>
		</div>
		<div class="input-field">
			<input name="priimek" type="text" id ="priimek">
			<label for="priimek">Priimek</label>
		</div>
		<div>
			<label>Datum rojstva</label>              
			<input type="date" name = "datum_rojstva" id = "datum_rojstva" class="datepicker">
		</div> 	
		<br>
		<label>Spol: </label>
		<p>
		  <input class="with-gap" name="spol" type="radio" id="M" value="M" />
		  <label for="M">Moški</label>
		</p>
		<p>
		  <input class="with-gap" name="spol" type="radio" id="F" value="F" />
		  <label for="F">Ženska</label>
		</p>
		<br>
		<button class="btn waves-effect waves-light" type = "submit" > Poišči </button>
	</form>
	<br>
 </div>
</div>
