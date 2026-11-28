#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function get (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      return callback(error);
    }
    try {
      callback(null, JSON.parse(body));
    } catch (e) {
      callback(e);
    }
  });
}

function printCharacters (urls, index) {
  if (index >= urls.length) {
    return;
  }
  get(urls[index], (error, character) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(character.name);
    printCharacters(urls, index + 1);
  });
}

get(filmUrl, (error, film) => {
  if (error) {
    console.error(error);
    return;
  }
  printCharacters(film.characters || [], 0);
});
