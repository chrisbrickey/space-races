const root = document.getElementById("innershell");

var innerDiv1 = document.createElement('div');
innerDiv1.className += "landingDiv"
root.appendChild(innerDiv1);

var p1 = document.createElement('p');
p1.className += "landingText";
p1.innerHTML += "This is the landing page for the work-in-progress web version of Space Races.";
innerDiv1.appendChild(p1);

var aTag = document.createElement('a');
aTag.className += "landingText";
aTag.setAttribute("href","https://github.com/chrisbrickey/space-race-game");
aTag.setAttribute("id","linkButton");
aTag.innerHTML += "Download command line version";

innerDiv1.appendChild(aTag);





