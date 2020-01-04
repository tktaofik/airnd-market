from datetime import datetime, date

from .db import job


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def get_create_job_properties():
    properties = job.columns.keys()
    properties.remove('id')
    properties.remove('updatedAt')
    properties.remove('createdAt')
    return properties
