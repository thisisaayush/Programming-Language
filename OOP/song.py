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

