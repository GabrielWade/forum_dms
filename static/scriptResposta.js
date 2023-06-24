function adicionarInput() {
  var divInputGroup = document.createElement("div");
  divInputGroup.className = "input-group";

  var spanInputGroupText = document.createElement("span");
  spanInputGroupText.className = "input-group-text";
  spanInputGroupText.textContent = "Resposta:";

  var textareaInput = document.createElement("textarea");
  textareaInput.className = "form-control";
  textareaInput.setAttribute("aria-label", "With textarea");

  divInputGroup.appendChild(spanInputGroupText);
  divInputGroup.appendChild(textareaInput);

  var divInput = document.querySelector(".input-group");
  divInput.parentNode.insertBefore(divInputGroup, divInput.nextSibling);
}
