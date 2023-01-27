function dienas() {
    var nosaukumi = new Array();
    nosaukumi[0] = "svētdienā";
    nosaukumi[1] = "pirmdienā";
    nosaukumi[2] = "otrdienā";
    nosaukumi[3] = "trešdienā";
    nosaukumi[4] = "ceturtdienā";
    nosaukumi[5] = "piektdienā";
    nosaukumi[6] = "sestdienā";
    var ievade = prompt("Ievadi datumu norādītajā formā:", "10/13/2016");
    var dzimis = new Date(ievade);
    var diena = dzimis.getDay();
    alert("Tu piedzimi " + nosaukumi[diena] + ".");
}