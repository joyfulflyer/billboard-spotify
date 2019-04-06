import logging
from chart import Chart
from entry import Entry


logger = logging.getLogger(__name__)


def save_chart(chart, Session, on_saved=None):
    session = Session()
    db_chart = Chart(type=chart.name,
                     date_string=chart.date,
                     next_chart_date=chart.nextDate)
    session.add(db_chart)
    try:
        session.commit()
    except Exception as err:
        logger.error("caught a integrety error '{0}'".format(err))
        return

    rowId = db_chart.id
    for entry in chart.entries:
        e = Entry(name=entry.title,
                  artist=entry.artist,
                  place=entry.rank,
                  peak_position=entry.peakPos,
                  last_position=entry.lastPos,
                  weeks_on_chart=entry.weeks,
                  chart_id=rowId)
        session.add(e)
    session.commit()
    if on_saved is not None:
        on_saved(chart.date)
