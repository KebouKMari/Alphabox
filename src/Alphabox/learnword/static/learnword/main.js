$( document ).ready(function() {
  	
    $(".cta").click(function() {
     $("form").toggle();
     // if form is visible
     if ($("form").is(":visible")) {
       // change .cta cursor to default
       $(".cta").css('cursor', 'default');
     }
     $(".cta1").click(function() {
      $("#lettre").toggle();
      // if form is visible
      if ($("#lettre").is(":visible")) {
        // change .cta cursor to default
        $(".cta1").css('cursor', 'default');
      }
   });
});

});