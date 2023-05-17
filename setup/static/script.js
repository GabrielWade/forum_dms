// Importar o jQuery
var scriptJQuery = document.createElement('script');
scriptJQuery.src = "https://code.jquery.com/jquery-3.6.0.min.js";
document.head.appendChild(scriptJQuery);

// Função a ser executada após o carregamento do jQuery
scriptJQuery.onload = function() {
  // Importar o Select2
  var scriptSelect2 = document.createElement('script');
  scriptSelect2.src = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js";
  document.head.appendChild(scriptSelect2);

  // Função a ser executada após o carregamento do Select2
  scriptSelect2.onload = function() {
    $(document).ready(function() {
      $(".select2").select2();
    });
  };
};
