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
     <a href ="http://127.0.0.1:8080/celice/poisci/" class="black-text collection-item"> Sojetniki </a> 	
     <a href ="http://127.0.0.1:8080/celice/proste/" class="black-text collection-item"> Proste celice </a> 		
     <a href ="http://127.0.0.1:8080/celice/zamenjaj/" class="black-text collection-item active"> Zamenjaj celice </a> 		 
 </div>
 </div>
 <div class = "col s8">
  <p>Če imata sojetnika težave, lahko enegga izmed nju premestimo v drugo celico.</p>
  <br>
  <form action = "/celice/zamenjaj/" method = "post">
   <div class="input-field">
    <input type = "text" name = "id_zapornika">
    <label for="id_zapornika">Id zapornika</label>
   </div>
   <div class="input-field">
    <input type = "text" name = "st_celice">
    <label for="st_celice">Številka celice</label>
   </div>
   <button class="btn waves-effect waves-light" type = "submit"> Zamenjaj </button>
  </form>
  <br>
  <br>
  <br>
 </div>
</div>