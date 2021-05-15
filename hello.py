<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Test API Client</title>
<script>
let doIt=()=>{
  let tab=document.getElementById("tab1");
  let rows=tab1.getElementsByTagName('tr');
  fetch('https://ash.dbsprojects.ie:8080/')
    .then(response => response.json())
    .then(data=>data.Results.forEach(  //.slice(0,3)
      x=>{
        let newRow=rows[0].cloneNode(true);
        let divs=newRow.getElementsByTagName('td');
        divs[0].innerHTML=x['ID'];
        divs[1].innerHTML=x['Name'];
        divs[2].innerHTML=x['Email'];
        tab1.appendChild(newRow);
      }
    )
  );
}
</script>
</head>
<body>
<button onClick="doIt()">Press me</button>
This is where the results turn up: <br/>
<table id='tab1' bgcolor='blue'>
<tr><td>ID</td><td>Name</td><td>Email</td></tr>
</table></body>
</html>
