FROM python:3.8.12-buster

COPY app.py /app/app.py
COPY setosa.jpg /app/setosa.jpg
COPY versi.jpg /app/versi.jpg
COPY virginica.jpg /app/virginica.jpg
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# set the working directory in the container to be /app
WORKDIR /app

# install the packages from the Pipfile in the container
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# execute the command python main.py (in the WORKDIR) to start the app
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
