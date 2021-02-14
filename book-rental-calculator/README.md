# Python-Flask Book Rental Calculator
This is a simple book rental calculator app

### To install the dependencies and run the application
For steps to run the application, please refer to [this file](steps.md)

### Initial DB creation
As this project is using a sqlite database, we need to create a file which can be used as storage for our database

**Note**: Please make sure you completed the above "dependencies" section to proceed further.

1 Create a file for database with the environment specific database name
```bash
source envs/dev
touch db/$DATABASE_NAME
``` 

2 

a. Initialize the migrations folder for database related changes and information.

b. run the migrate command to generate the migration script contains DB schema(for First time) and changes in schema(from Second time onwards)

```bash
python migrate.py db init
python migrate.py db migrate
```
c. Make any required changes in the generated migration script and run the following command
```bash
python migrate.py db upgrade
```

### Run the application
```bash
Python app.py
```

### Unittests

The **tests** folder contains unittest files.

Run the following command to run all the files in this **test** folder
```bash
coverage run -m unittest discover -s tests/ -p 'test_*.py'
```

To see the report generated over the run command, run the following command
```bash
coverage report
```

### Dockerize the application
Go to the root folder of this project( where Dockerfile is located).

1 To build
```
docker build -t <custom_image_name> .
```
2 To create container from the created image
```bash
docker run --name <custom_container_name> --env-file book-rental-calculator\envs\dev -d -p 5020:5020 <img_id>
```
As we have redirected the port from container port to HOST machine port using **-p** command, 
now we can access the application in the container form the localhost browser (http://127.0.0.1:5020).

3 To create tage for this image
```bash
docker tag <img_id> <tag-nameeg:4329/python-flask-book-rental-calculator:1.1.0>
```
4 To push this image to our docker hub repository
```bash
docker push <tag-name eg: 4329/python-flask-book-rental-calculator:1.1.0>
```
**Note:** Don't forget to do "Docker login" before pushing the image 
