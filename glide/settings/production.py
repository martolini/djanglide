DEBUG = False

with open('/home/glide/web/glide/glide/settings/db.txt', 'rb') as f:
    db_password = f.readline()
db_password = db_password.replace("\n","").strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'glidemain',
        'USER': 'glide',
        'PASSWORD': db_password,
        'HOST': '127.0.0.1',
    }
}
