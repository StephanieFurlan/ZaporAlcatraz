%rebase('osnova.tpl')
<div class = "row">
 <nav>
  <div class = "nav-wrapper teal lighten-1">
   <ul class= "hide-on-med-and-down right">
    <li><a href ="http://127.0.0.1:8080/" class ="white-text"><i class = "material-icons">home</i> </a></li>
   </ul>  
  </div>
 </nav>
 <div class="col s3">
 <div class = "collection">
     <a href ="http://127.0.0.1:8080/zaporniki/" class="black-text collection-item active"> Poišči zapornika </a> 
     <a href ="http://127.0.0.1:8080/zaporniki_kazniva_dejanja/" class="black-text collection-item"> Kazniva dejanja zapornika </a> 
 </div>
 </div>
 <div class = "col s9">
  <p>Poišči zapornika tako, da vneses njegov ID.</p>
  <br>
  <form action = "/zaporniki_poisci/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
  <br>
  <br>
  <br>
% if ime is None:
   <p> Zapornik z id-jem <b>{{vnos}}</b> ne obstaja. </p>
% else:
   <ul class="collection">
     <li class="collection-item"><big><b>Ime:   </b>{{ime}}</big></li>
     <li class="collection-item"><big><b>Priimek:   </b>{{priimek}}</big></li>
     <li class="collection-item"><big><b>Datum rojstva:   </b>{{datum_rojstva}}</big></li>
     <li class="collection-item"><big><b>Spol:   </b>{{spol}}</big></li>
     <li class="collection-item"><big><b>Celica:   </b>{{celica}}</big></li>
   </ul>
% end
 </div>
</div>
