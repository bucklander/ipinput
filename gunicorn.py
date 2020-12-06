"""
WSGI entry-point file
"""

bind = '0.0.0.0:5017'
chdir = '/opt/ipinput'

workers = 8
worker_class = 'sync'
timeout = 300

accesslog = '-'
access_log_format = '%(t)s %(p)s %(h)s %({X-Forwarded-For}i)s %(l)s "%(r)s" %(s)s %(b)s "%(f)s"'
