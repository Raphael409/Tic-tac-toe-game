function startGame() {
  alert("Restart the game??");
  clearButtons("btn1");
  clearButtons("btn2");
  clearButtons("btn3");
  clearButtons("btn4");
  clearButtons("btn5");
  clearButtons("btn6");
  clearButtons("btn7");
  clearButtons("btn8");
  clearButtons("btn9");
}

function clearButtons(buttonId) {
  const element = document.getElementById(buttonId);
  element.innerHTML = "";
  element.classList.remove("buttons-color-blue");
  element.classList.remove("buttons-color-red");
}
// document.getElementById("btn1").addEventListener("click", function() {
//   document.getElementById("btn1").innerHTML = "X";
//   this.style.backgroundColor = "red";
// });
// document.getElementById("btn2").addEventListener("click", function() {
//   document.getElementById("btn2").innerHTML = "O";
//   this.style.backgroundColor = "blue";
// });

// document.getElementById("btn3").addEventListener("click", function() {
//   document.getElementById("btn3").innerHTML = "X";
//   this.style.backgroundColor = "red";
// });
// document.getElementById("btn4").addEventListener("click", function() {
//   document.getElementById("btn4").innerHTML = "O";
//   this.style.backgroundColor = "blue";
// });
// document.getElementById("btn5").addEventListener("click", function() {
//   document.getElementById("btn5").innerHTML = "X";
//   this.style.backgroundColor = "red";
// });
// document.getElementById("btn6").addEventListener("click", function() {
//   document.getElementById("btn6").innerHTML = "O";
//   this.style.backgroundColor = "blue";
// });
// document.getElementById("btn7").addEventListener("click", function() {
//   document.getElementById("btn7").innerHTML = "X";
//   this.style.backgroundColor = "red";
// });
// document.getElementById("btn8").addEventListener("click", function() {
//   document.getElementById("btn8").innerHTML = "O";
//   this.style.backgroundColor = "blue";
// });
// document.getElementById("btn9").addEventListener("click", function() {
//   document.getElementById("btn9").innerHTML = "X";
//   this.style.backgroundColor = "red";
// });

// document.getElementsByClassName("buttons").addEventListener("click", function2);
// function function2() {
//   document.getElementById("btn").innerHTML = "O";
// }

let isPlayer1 = true;
function updateButtons(buttonId) {
  const element = document.getElementById(buttonId);
  if (isPlayer1) {
    element.innerHTML = "X";
    element.classList.remove("buttons-color-blue");
    element.classList.add("buttons-color-red");
  } else {
    element.innerHTML = "O";
    element.classList.remove("buttons-color-red");
    element.classList.add("buttons-color-blue");
  }
  isPlayer1 = !isPlayer1;
}
