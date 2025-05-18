from datetime import datetime


def datetime_serialize(data):
    if isinstance(data, datetime):
        return data.isoformat(timespec="seconds")
    else:
        return data
