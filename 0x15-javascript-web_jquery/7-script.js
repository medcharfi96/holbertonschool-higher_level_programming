const $salem = window.$;
const AdressURL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$salem.getJSON(AdressURL, function (inform) {
  $salem('#character').text(inform.name);
});
