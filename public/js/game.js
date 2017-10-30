const root = document.getElementById("innershell");

var innerDiv1 = document.createElement('div');
innerDiv1.className += "landingDiv"
root.appendChild(innerDiv1);

var p1 = document.createElement('p');
p1.className += "landingText";
p1.innerHTML += "This is the landing page for the Space Races web game which is a work-in-progress.";
innerDiv1.appendChild(p1);


var innerDiv2 = document.createElement('div');
innerDiv2.className += "landingDiv"
root.appendChild(innerDiv2);

var p2 = document.createElement('div');
p2.className += "landingText";
p2.innerHTML += "Play the game from the command line by downloading the files here: ";

var aTag = document.createElement('a');
aTag.className += "landingText";
aTag.setAttribute("href","https://github.com/chrisbrickey/space-race-game");
aTag.setAttribute("id","githubLink");
aTag.innerHTML += "space races on github";


innerDiv2.appendChild(p2);
innerDiv2.appendChild(aTag);





