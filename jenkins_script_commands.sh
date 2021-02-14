
# this alone is not sufficient for jenkins, jenkins configuration on the server/local has to be made manually.

# but these below commands are what needed in the jenkins' pipeline configure's execute shell section to build the code.

CONTAINER_NAME=python-flask-book-rental-calculator:latest

# stopping all containers built from this image
docker ps -a | awk '{print $1, $2}' | grep python-flask-book-rental-calculator:latest | awk '{print $1}' | xargs -n 1 docker stop

# removing all containers built from this image
docker ps -a | awk '{print $1, $2}' | grep python-flask-book-rental-calculator:latest | awk '{print $1}' | xargs -n 1 docker rm

# just printing list of files and directories on pwd
ls -la

# just printing docker version
docker --version

# building image from the repo
docker build -t python-flask-book-rental-calculator:latest .

# creating container from the image built
docker run --name flask-book-app --env-file book-rental-calculator/envs/dev -d -p 5020:5020 python-flask-book-rental-calculator:latest

