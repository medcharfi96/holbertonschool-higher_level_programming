const $salem = window.$;
$salem('#toggle_header').click(function () {
  if ($salem('HEADER').hasClass('green')) {
    $salem('HEADER').removeClass('green');
    $salem('HEADER').addClass('red');
  } else {
    $salem('HEADER').removeClass('red');
    $salem('HEADER').addClass('green');
  }
});
