function startGame() {
  alert("Restart the game??");
}
document.getElementById("btn1").addEventListener("click", function() {
  document.getElementById("btn1").innerHTML = "X";
  this.style.backgroundColor = "red";
});
document.getElementById("btn2").addEventListener("click", function() {
  document.getElementById("btn2").innerHTML = "O";
  this.style.backgroundColor = "blue";
});

document.getElementById("btn3").addEventListener("click", function() {
  document.getElementById("btn3").innerHTML = "X";
  this.style.backgroundColor = "red";
});
document.getElementById("btn4").addEventListener("click", function() {
  document.getElementById("btn4").innerHTML = "O";
  this.style.backgroundColor = "blue";
});
document.getElementById("btn5").addEventListener("click", function() {
  document.getElementById("btn5").innerHTML = "X";
  this.style.backgroundColor = "red";
});
document.getElementById("btn6").addEventListener("click", function() {
  document.getElementById("btn6").innerHTML = "O";
  this.style.backgroundColor = "blue";
});
document.getElementById("btn7").addEventListener("click", function() {
  document.getElementById("btn7").innerHTML = "X";
  this.style.backgroundColor = "red";
});
document.getElementById("btn8").addEventListener("click", function() {
  document.getElementById("btn8").innerHTML = "O";
  this.style.backgroundColor = "blue";
});
document.getElementById("btn9").addEventListener("click", function() {
  document.getElementById("btn9").innerHTML = "X";
  this.style.backgroundColor = "red";
});

document.getElementsByClassName("buttons").addEventListener("click", function2);
function function2() {
  document.getElementById("btn").innerHTML = "O";
}

/*document
  .getElementsByClassName("buttons")
  .addEventListener("click", function() {
    document.getElementById("btn1").innerHTML = "X";
    this.style.backgroundColor = "blue";
  });*/
