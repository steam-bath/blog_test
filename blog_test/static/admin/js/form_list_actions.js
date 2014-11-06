$(document).ready(function () {

    //аяксовое переключение активности у элемента в списке административного интерфейса
    $('a._is_active').on('click', function(){
        var image = $(this).find('img');
        image.attr('src', '/static/admin/img/icons/icon-loader.gif');

        $.ajax({
				url: "change_activity/",
				type: "POST",
				data: ({
					element_id: $(this).find('input[name="element_id"]').val()
				}),
				success: function(data){
                    image.attr('src', data.icon).attr('alt', data.alt);
					if(data.result != 1)
						alert('Произошла ошибка при смене активности !');
				}
			});
    });

});