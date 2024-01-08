This is a Template for a Flask Application running over Docker and using Gunicorn for a reverse proxy NGINX server with a wsgi entrypoint.

Test-
docker-compose run test #To test everything
docker-compose run test pytest tests/integration    #To test just 1 folder