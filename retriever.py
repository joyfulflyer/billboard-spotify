import logging
from chart import Chart
from entry import Entry
from sqlalchemy import desc


def get_latest_chart(Session, type='hot-100'):
    session = Session()
    q = session.query(Chart).filter_by(type=type).order_by(
        desc(Chart.date_string))
    return q.first()


