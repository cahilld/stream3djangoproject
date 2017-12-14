'use strict';

function on_move_card(card) {
    console.log(card);
}

dragula([$('#P')[0], $('#I')[0], $('#D')[0], $('#A')[0]])
  .on('drag', function (el) {
    el.className = el.className.replace('ex-moved', '');
  })
  .on('drop', function (el, target) {
    $.ajax({
      type: "POST",
      url: 'https://stream3-djangoproject-desc.c9users.io/move/',
      data: { 'id': el['id'], 'status': target['id'] },
      headers: { 
          "X-CSRFToken": csrf_token 
      },
      success: on_move_card,
      dataType: 'json'
    });
  })
  .on('over', function (el, container) {
    container.className += ' ex-over';
  })
  .on('out', function (el, container) {
    container.className = container.className.replace('ex-over', '');
  });
