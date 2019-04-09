import logging
from models.chart import Chart
from models.entry import Entry
from models.song import Song
from sqlalchemy import desc
import time


logger = logging.getLogger(__name__)


def create_in_loop(Session, total=10000, loops=10):
    start_time = time.time()
    logger.error("Start time: %r" % (start_time,))
    session = Session()
    for x in range(loops):
        entry_query = session.query(Entry) \
            .filter(Entry.song_id.is_(None)) \
            .limit(total/loops)
        if entry_query.count() == 0:
            raise Error("All done")
        for entry in entry_query:
            song_query = session.query(Song.id).filter(
                Song.name == entry.name, Song.artist == entry.artist)
            song_count = song_query.count()
            db_song = 0
            if song_count > 1:
                raise Error("Too many songs! Query: %s" % (song_query,))
            elif song_count == 0:
                db_song = create_song(entry.name, entry.artist, session)
            else:
                db_song = song_query.first()
            entry.song_id = db_song.id
            session.commit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.error("Elapsed time: %s" % (elapsed_time,))


def create_songs(Session, count=100):
    start_time = time.time()
    session = Session()
    entry_query = session.query(Entry).filter(
        Entry.song_id.is_(None)).limit(count)
    if entry_query.count() == 0:
        raise Error("All done")
    for entry in entry_query:
        song_query = session.query(Song.id).filter(
            Song.name == entry.name, Song.artist == entry.artist)
        song_count = song_query.count()
        db_song = 0
        if song_count > 1:
            raise Error("Too many songs! Query: %s" % (song_query,))
        elif song_count == 0:
            db_song = create_song(entry.name, entry.artist, session)
        else:
            db_song = song_query.first()
        entry.song_id = db_song.id
        session.commit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.error("Elapsed time: %s" % (elapsed_time,))


def create_song(name, artist, session):
    new_song = Song(name=name, artist=artist)
    session.add(new_song)
    session.commit()
    return new_song
