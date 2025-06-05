from src.domain.model import Movie, Theater
from src.domain.errors import DuplicateMovieName
from datetime import timedelta
import pytest
from test.builder.movie_builder import MovieBuilder

def test_sucessfully_creates_movie():
    movie = Movie("MovieName",90)
    assert movie is not None
    
def test_movie_has_unique_title():
    theater = Theater()
    movie1 = Movie("MovieName",90)
    movie2 = Movie("MovieName",90)
    theater.addMovie(movie1)
    with pytest.raises(DuplicateMovieName):
        theater.addMovie(movie2)
        
def test_return_formatted_movie_duration():
    movie1 = Movie("MovieName",30)
    assert movie1.get_duration() == "30min"
    movie2 = Movie("MovieName",90)
    assert movie2.get_duration() == "1h30min"
    movie3 = Movie("MovieName",120)
    assert movie3.get_duration() == "2h"
    
def test_return_movie_timedelta():
    movie = Movie("MovieName",170)
    movie2 = MovieBuilder().aMovie().with_duration(200).build()
    assert movie.get_timedelta() == timedelta(minutes=170)
    assert movie2.get_timedelta() == timedelta(minutes=200)