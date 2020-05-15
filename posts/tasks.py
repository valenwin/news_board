from celery.task import periodic_task
from celery.schedules import crontab

from .models import Post


@periodic_task(run_every=crontab(minute=0, hour='23'))
def reset_post_upvotes():
    """
    Task for recurring job running once a day
    to reset post upvotes count.
    """
    Post.objects.update(upvotes=0)
