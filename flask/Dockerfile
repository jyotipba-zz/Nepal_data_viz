# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install flask bokeh

ENV FLASK_APP run.py

EXPOSE 5000
# run the command to start flask server
CMD ["flask", "run", "--host", "0.0.0.0"]
