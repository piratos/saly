import os
import random


def populate():

    print 'Populating Database...'
    print '----------------------\n'

    username = 'root'
    email = 'uname@domain.com'
    password = 'rootroot'
    status = ['stuck', 'done', 'in progress', 'canceled']


    root = create_super_user(username, email, password)
    for i in range(10):
        add_task('task %d' % i, random.choice(range(10)), 'this is the %dth note' % i, random.choice(status), root)


def add_task(name, priority, note, status, user):
    g, created = ToDoTask.objects.get_or_create(user=user, name=name, priority=priority, note=note, status=status)
    print '- Task: {0}, Created: {1}'.format(priority, str(created))
    return g


def create_super_user(username, email, password):
    '''
    for some reason get_or_create didn't work with creating the
    SuperUser so here is a try/except, with an IntegrityError
    raised if the SuperUser already exists
    '''
    try:
        u = User.objects.create_superuser(username, email, password)
        return u
    except IntegrityError:
        return None

if __name__ == '__main__':
    print '\n' + ('=' * 80) + '\n'
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'doitnow.settings')
    django.setup()
    from tasks.models import ToDoTask
    from django.contrib.auth.models import User
    from django.db import IntegrityError
    populate()