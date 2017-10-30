const root = document.getElementById("innershell");

var innerDiv1 = document.createElement('div');
var innerDiv2 = document.createElement('br');
var innerDiv3 = document.createElement('div');

innerDiv1.className += "landingText";
innerDiv2.className += "landingText";
innerDiv3.className += "landingText";

root.appendChild(innerDiv1);
root.appendChild(innerDiv2);
root.appendChild(innerDiv3);

innerDiv1.innerHTML += "This is the landing page for the Space Races web game which is a work-in-progress.";
innerDiv3.innerHTML += "Play the game from the command line by downloading the files here: https://github.com/chrisbrickey/space-race-game";