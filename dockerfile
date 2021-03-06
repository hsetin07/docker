# set base image (host OS)
FROM python:3.9
# set the working directory in the container
WORKDIR /Docker
COPY . .
RUN pip install flask
# command to run on container start
CMD [ "python", "./app.py" ]



