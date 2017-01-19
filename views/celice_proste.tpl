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
     <a href ="http://127.0.0.1:8080/celice/proste/" class="black-text collection-item active"> Proste celice </a> 	
     <a href ="http://127.0.0.1:8080/celice/zamenjaj/" class="black-text collection-item"> Zamenjaj celice </a> 	
</div>
	</div>
	<div class = "col s8">
	<br>
	<b>Vse proste ženske celice so:</b>
	%z = 0
  	%for (celica, st_prostih_postelj) in zenske[0:-1]:
		{{celica}},
		%z = z + st_prostih_postelj
	%end
	{{zenske[-1][0]}}.
	%z = z + 1
	%z = z + zenske[-1][1]
	<br>
	<br>
	<b>Vse proste moške celice so:</b>
	%m = 0
  	%for (celica, st_prostih_postelj) in moske[0:-1]:
		{{celica}},
		%m = m +st_prostih_postelj
	%end
	{{moske[-1][0]}}.
	%m = m + 1
	%m = m + moske[-1][1]
	<br>
	<br>
	<br>
    <table>
        <thead>
          <tr>
              <th></th>
              <th>Ženske celice</th>
              <th>Moške celice</th>
			  <th>Skupaj</th>
          </tr>
        </thead>
		<tbody>
			<tr>
				<td><b>Število prostih celic</b></td>
				<td>{{len(zenske)}}</td>
				<td>{{len(moske)}}</td>
				<td>{{len(zenske)+len(moske)}}</td>
            </tr>
			<tr>
				<td><b>Število prostih ležišč</b></td>
				<td>{{z}}</td>
				<td>{{m}}</td>
				<td>{{z + m}}</td>
			</tr>
		</tbody>
	</table>			
 </div>
 </div>