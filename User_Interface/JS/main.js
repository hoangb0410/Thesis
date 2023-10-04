var selectedTextbox;

function selectTextbox(textboxNumber) {
  selectedTextbox = textboxNumber;
}

function appendNumber(number) {
  var textbox = document.getElementById("textbox" + selectedTextbox);
  textbox.value += number;
}

function clearDisplay() {
  var textbox = document.getElementById("textbox" + selectedTextbox);
  textbox.value = "";
}