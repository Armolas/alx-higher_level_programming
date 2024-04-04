$(document).ready(function(){
	$("input#btn_translate").on("click", translate);
	$("input#language_code").on("keypress", function(event){
		if (event.which == 13){
			translate();
		}
	});
	function translate(){
		const lang = $("input#language_code").val();
		$.get("https://hellosalut.stefanbohacek.dev/?lang="+lang, function(data){
			$("div#hello").text(data.hello);
		});
	}
});
