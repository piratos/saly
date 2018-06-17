import os
import random


def populate():

    print ' -----------------------\n'
    print '| Populating Database...|'
    print ' -----------------------\n'

    username = 'root'
    email = 'uname@domain.com'
    password = 'rootroot'
    status = ['stuck', 'done', 'in progress', 'canceled']


    users = User.objects.filter(username='root')
    if users:
        root = users[0]
    else:
        root = create_super_user(username, email, password)
    print 'super user created', root
    project = Project.objects.get_or_create(user=root, name='household', status='active')[0]
    print 'project created ',project
    for i in range(10):
        add_task('task %d' % i, random.choice(range(10)), 'this is the %dth note' % i, random.choice(status), project)


def add_task(name, priority, note, status, project):
    g, created = ToDoTask.objects.get_or_create(project=project, name=name, priority=priority, note=note, status=status)
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
    from tasks.models import ToDoTask, Project
    from django.contrib.auth.models import User
    from django.db import IntegrityError
    populate()
