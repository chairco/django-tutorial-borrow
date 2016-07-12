(function ($) {
$('#cocoModal').on('show.bs.modal', function( event ) {
  var button = $(event.relatedTarget)
  var recipient = button.data('whatever') 
  var modal = $(this)
  modal.find('.modal-title').text('New to ' + recipient)
  $('#cocosave').click(function( event ) {
    var name = modal.find("input[name='name']").val();
    var email = modal.find('input[name="email"]').val();
    $.ajax({
      type: "post",
      url: "/adddri_coco",
      cache: false,
      data: {
        name: name, 
        email: email,
      },
      dataType: "html",
      success: function(data, result, statues, xml){
        alert("儲存中...請按確定繼續");
        if (data == "False"){
          $("#statusModal").modal({show: true}).find('.modal-body').text("EMAIL格式存在錯誤 或是 使用者名稱已經存在CoCo's GROUP, 請確認.");
          } else {
          $("#statusModal").modal({show: true}).find('.modal-body').text("更新成功");
          $('#id_cocodri').append('<option value="'+data+'">'+name+', '+email+'</option>');
          }
      }
    });
    event.stopPropagation();
    //$('#cocosave').stopPropagation()
  });
});
})(jQuery);