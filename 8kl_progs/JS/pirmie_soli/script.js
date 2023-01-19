    
    
    
document.getElementById("pirmais").innerHTML = "Pirmais piemers";
document.getElementById("pirmais").style.fontSize = "25px";
document.getElementById("pirmais").style.color = "red";
document.getElementById("pirmais").style.backgroundColor = "yellow";

function changeImage() {var image = document.getElementById('lighbulb');
          if (image.src.match("bulbon")) {image.src = "pic_bulboff.gif";} 
          else {image.src = "pic_bulbon.gif";}}

window.onload = init;

function init(){var button = document.getElementById("addButton")button.onclick = handleButtonClick;}
      
function handleButtonClick() {alert("Вы нажали на кнопку");}

document.getElementById('first-button').addEventListener('click', () => open('./autors.html'));


