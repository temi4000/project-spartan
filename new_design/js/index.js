$('#show-reviews').click(function(){
  $('.review-card').slideToggle();
});

$('#edit-profile-btn').click(function(){
  $('#card-edit-profile').slideToggle();
});














































































var faqList = $('#faq-list');
var faqElements = faqList.children().length;
faqList.children().find('span').hide();
var arrow = faqList.children().find('i');

for(var i = 0; i <= faqElements; i++){
	arrow.addClass("glyphicon glyphicon-play faq-icon");
}
$('.form-group').on('click', function(){
	$(this).find('span').toggle();
});



































