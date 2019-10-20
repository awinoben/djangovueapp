# frontpage

> A Django-Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```
# backend

>Here we set-up Django Backend:


``` bash
# setup database connections:

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'databasename',
      'USER': 'databaseuser',
      'PASSWORD': 'yourpassword',
      'HOST': 'localhost',
      'PORT': 22222,
   }
}


# Google authentication:

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '[your google auth key]'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '[your google auth secret key]'

    In main.js, stored in frontpage/src folder find:

Vue.use(VueAuthenticate, {
  providers: {
    google: {
      clientId: 'yourgooglecliendID',
      redirectUri: 'http://localhost:8080/',
      url: 'http://localhost:8000/api/login/social/token_user/google/',
    }
  }
});

# Running template

To run the project after installation, open two consoles and in the first one, go to the hospital folder and run:

python manage.py runserver

# and then in the second console - go to the frontpage folder and run:

npm run dev
```