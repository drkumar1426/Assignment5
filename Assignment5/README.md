# RESTful-web-service using DOCKER container
A docker container running flask python environment shows a good RESTful API example

Requests:

1. /restaurants
2. /restaurants/10
3. /restaurants/rating/4
3. /restaurants/type/chinese

-Setup the project with the app.py and JSON file in a single folder.

-Create Docker Image by running : "docker build -t docker-python ."

-Check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 5000:5000 docker-python"