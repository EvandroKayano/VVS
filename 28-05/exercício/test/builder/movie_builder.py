from src.domain.model import Movie

class MovieBuilder:
    '''
    Por padrão movie = "Die Hard 2" duration = 124
    '''
    movie: Movie
    
    def __init__(self):
        self.movie = Movie("Die Hard 2", 124)  
          
    def aMovie(self):
        self.movie = Movie("Die Hard 2", 124)
        return self
        
    def build(self):
        return self.movie

         
    def with_duration(self, duration):
        self.movie.duration = duration
        return self