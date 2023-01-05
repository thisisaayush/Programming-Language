class Song:
    """
    Class to represent a Song

    Attributes:
        title(str): The title of the Song
        artist(Artist): An artist object representing the song creator.
        duration(int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """
        :param title: Initialises the 'title' attribute.
        :param article: At Artist object representing the song's creator.
        :param duration: Initial value for the 'duration' attribute.
        """

        self._title = title
        self._artist = artist
        self._duration = duration

class Album:
    """Class to represent an Album, using it's track list

        Attributes:
            album_name(str): The name of the album.
            year(int): The year was album was released.
            artist: Artist who created the album.

        Methods:
            addSong: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.year = Artist("Various Artists.")
        else:
            self.artist = artist

        self.tracks=[]

    def add_song(self, song, position=None):
        """
        Adds a song to the track list.

        :param song:
        :param position:
        :return:
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position,song)


class Artist:
    """
    Basic class to store artist details

    Atributes:
        name(str): The name of the artist.
        albums(List[Album]): A list of the albums by this artist.
        The list includes only those albums in this collection, it is
        not an exhaustive list of the artist's published albums.

    Methos:
        add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.
            Args:
                album(Album): Album object to add to the list.
        """
        self.albums.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row consists of (artist, album, year, song).
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

        if new_artist is None:
            new_artist = Artist(artist_field)
        elif new_artist.name != artist_field:
            #Just read details for a new artist.
            #Store the current album in the current artist's collection
            #then create a new artist object.

            new_artist.add_album(new_album)
            artist_list.append(new_artist)
            new_artist = Artist(artist_field)
            new_album = None

        if new_album is None:
            new_album = Album(album_field, year_field, new_artist)
        elif new_album.name != album_field:
            #Just read a new album for the current artist.
            #Store the current album in the artist's collection
            #then create a new album object.
            new_artist.add_album(new_album)
            new_album = Album(album_field, year_field, new_artist)

        new_song = Song(song_field, new_artist)
        new_album.add_song(new_song)

        #After read the last line of the text file, we will have an artist and album that
        #haven't been store- process them now.
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list



if __name__ == "__main__":
    artist = load_data()
    print("There are {} artists.".format(len(artist)))