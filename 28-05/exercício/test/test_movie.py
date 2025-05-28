from src.domain.model import Movie, Theater
from src.domain.errors import DuplicateMovieName
from datetime import timedelta
import pytest

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
    movie = Movie("MovieName",90)
    assert movie.get_duration() == "1h30min"
    
def test_return_movie_timedelta():
    movie = Movie("MovieName",170)
    assert movie.get_timedelta() == timedelta(minutes=170)