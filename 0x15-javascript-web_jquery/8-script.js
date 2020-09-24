const $salem = window.$;
const ADressURL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$salem.get(ADressURL, function (info) {
  var i = 0;
  while (i < info.results.length) {
    $salem('ul#list_movies').append(`<li>${info.results[i].title}</li>`);
    i++;
  }
});
