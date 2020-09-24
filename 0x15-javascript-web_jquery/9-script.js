const $salem = window.$;
$salem.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (info) => {
  $salem('#hello').text(info.hello);
});
