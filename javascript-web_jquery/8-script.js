$.getJSON(
  "https://swapi-api.hbtn.io/api/films/?format=json",
  function (response) {
    response.results.forEach((movie) => {
      $("UL#list_movies").append(`<li>${movie.title}</li>`);
    });
  }
);
