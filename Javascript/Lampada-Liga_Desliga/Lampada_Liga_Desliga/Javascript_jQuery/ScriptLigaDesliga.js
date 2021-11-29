$(document).ready(function(){

  $("#botao").click(function(){

    if($("img").attr("src") == "lamp_on.gif"){
      $("img").attr("src", "lamp_off.gif");
      $("#botao").val("Ligar");
    }
    else{
      $("img").attr("src", "lamp_on.gif");
      $("#botao").val("Desligar");
    }
  });
});
