from src.domain.model import Room, Theater, Movie, Session
from src.domain.errors import DuplicateRoomName, DuplicateMovieName
import pytest

def test_can_add_room_to_theater():
    theater = Theater()
    room1 = Room("1")
    theater.add(room1)
    assert room1 in theater.rooms

def test_can_remove_room_from_theater():
    theater = Theater()
    room1 = Room("1")
    theater.add(room1)
    theater.remove(room1)
    assert room1 not in theater.rooms

def test_theater_room_has_unique_name():
    theater = Theater()
    room1 = Room("1")
    room2 = Room("1")
    theater.add(room1)
    with pytest.raises(DuplicateRoomName):
        theater.add(room2)
        
def test_can_add_movie_to_theater():
    theater = Theater()
    movie = Movie("MovieName",90)
    theater.addMovie(movie)
    assert len(theater.movies) == 1
    
def test_cannot_add_duplicate_movie():
    theater = Theater()
    movie1 = Movie("MovieName",90)
    movie2 = Movie("MovieName",90)
    theater.addMovie(movie1)
    with pytest.raises(DuplicateMovieName):
        theater.addMovie(movie2)
        
def test_can_remove_movie_from_theater():
    theater = Theater()
    movie = Movie("MovieName", 90)
    theater.addMovie(movie)
    theater.removeMovie(movie)
    assert movie is not theater.movies
    
def test_can_add_session():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName",90)
    theater.create_session(movie, room, "14:30")
    created_session = Session(movie, room, "14:30")
    assert created_session in theater.sessions
    
def test_can_remove_session():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName",90)
    session = theater.create_session(movie, room, "14:30")
    theater.remove_session(session)
    assert session is not theater.sessions