class Bucketlist():
    def __init__(self,Movies):
        self.Movies=Movies
    def listofmovies(self):
        print("Available Movies")
        for movie in Movies:
            print (movie)
    def borrowmovie(self,borrowmovie):
        if borrowmovie in self.Movies:
            print("You can Download")
            self.Movies.remove(borrowmovie)
        else:
            print("Movie is not available")
    def receivedmovie(self,receivedmovie):
        print("you have retuned the movie")
        self.Movies.append(receivedmovie)

Movies=["Red notice","6 Underground","Deadpool","Deadpool2"]
P=Bucketlist(Movies)
list="""
   1.Red notice
   2.6 Underground
   3.Deadpool
   4.Deadpool2
"""
while True:
    print(list)
    ch=input("List of movies")
    if ch == 1:
        P.listofmovies()
    elif ch == 2:
        print(Movies)
        Movie= input("enter the movie you want:")
        P.borrowmovies(movie)
    elif ch== 3:
        movie=input("enter the movie you wanna return:")
        P.receivedmovie(movie)
    else:
        print("thank you for using our service")
quit()


