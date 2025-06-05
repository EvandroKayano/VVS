from src.domain.model import Room, Session
from test.builder.movie_builder import MovieBuilder
from datetime import datetime

class SessionBuilder:
    '''
    Por padrão Room = "1" start_time = "16:30"
    '''
    session: Session
    
    
    def __init__(self):
        pass
          
    def aSession(self):
        self.session = Session(MovieBuilder().aMovie().build(), Room("1"), "16:30")
        return self
        
    def build(self):
        return self.session

    def with_movie(self, movie):
        self.session.movie = movie
        return self
    
    def with_room(self, room):
        self.session.room = room
        return self
    
    def with_start_time(self, start_time):
        self.session.start_time = datetime.strptime(start_time, "%H:%M")
        return self