FROM python:3.8

COPY . /app
# set a directory for the app
WORKDIR /app

# copy all the files to the container


# install dependencies
RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["uvicorn", "app:app", "--reload"]