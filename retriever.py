import logging
from models.chart import Chart
from models.entry import Entry
from sqlalchemy import desc


def get_latest_chart(Session, type='hot-100'):
    session = Session()
    q = session.query(Chart).filter_by(type=type).order_by(
        desc(Chart.date_string))
    return q.first()


def get_song_and_artists(Session):
    session = Session()
    q = session.query(Entry).group_by(Entry.name, Entry.artist)
    return q
