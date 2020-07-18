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
  document.getElementById("turns").innerText = "X's First move";
  isPlayer1 = true;
}

function clearButtons(buttonId) {
  const element = document.getElementById(buttonId);
  element.innerHTML = "";
  element.classList.remove("buttons-color-blue");
  element.classList.remove("buttons-color-red");
}
isPlayer1 = true;
function updateButtons(buttonId) {
  const element = document.getElementById(buttonId);
  if (isPlayer1) {
    document.getElementById("turns").innerText = "O";
    element.innerHTML = "X";
    element.classList.remove("buttons-color-blue");
    element.classList.add("buttons-color-red");
  } else {
    document.getElementById("turns").innerText = "X";
    element.innerHTML = "O";
    element.classList.remove("buttons-color-red");
    element.classList.add("buttons-color-blue");
  }
  isPlayer1 = !isPlayer1;
}

/*function getWinner() {
    var btn1 = document.getElementById(btn1),
      btn2 = document.getElementById(btn2),
      btn3 = document.getElementById(btn3),
      btn4 = document.getElementById(btn4),
      btn5 = document.getElementById(btn5),
      btn6 = document.getElementById(btn6),
      btn7 = document.getElementById(btn7),
      btn8 = document.getElementById(btn8),
      btn9 = document.getElementById(btn9);

    if (
      btn1.innerHTML === btn2.innerHTML &&
      btn1.innerHTML === btn3.innerHTML
    ) {
      alert("you won");
    }
  }
*/
