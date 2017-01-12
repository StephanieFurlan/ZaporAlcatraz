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
     <a href ="http://127.0.0.1:8080/zaporniki/" class="black-text collection-item"> Poisci zapornika </a> 
     <a href ="http://127.0.0.1:8080/zaporniki_kazniva_dejanja/" class="black-text collection-item active"> Kazniva dejanja zapornika </a> 
 </div>
 </div>
 <div class = "col s9">
  <p>Poisci zapornika tako, da vneses njegov ID.</p>
  <br>
  <form action = "/zaporniki_kazniva_dejanja/">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="first_name">Id zapornika</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Poišči </button>
  </form>
  <br>
  <br>
  <br>
   <ul class="collection">
     <li class="collection-item"><big><b>Ime:   </b>kaznivo dejanje</big></li>
   </ul>
 </div>
</div>
