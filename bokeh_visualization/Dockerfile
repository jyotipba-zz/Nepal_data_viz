# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install bokeh pandas geopandas


EXPOSE 5006

ENTRYPOINT ["bokeh","serve","run.py","--allow-websocket-origin=*"]
