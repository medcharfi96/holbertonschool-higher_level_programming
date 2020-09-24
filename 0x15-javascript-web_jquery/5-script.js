const $salem = window.$;
$salem(' #add_item').click(function () {
  $salem('ul.my_list').append('<li>Item</li>');
});
