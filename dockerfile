FROM continuumio/miniconda3

WORKDIR /app

LABEL maintainer="Jon Anwyl <jon.anwyl@gmail.com>"

ENV FLASK_APP=nunki-test-api.py

# Create the environment.
COPY environment.yml .
RUN conda env create -n nunki -f environment.yml

# define the port number the container should expose
EXPOSE 5000

COPY app .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "nunki", "python3", "-m", "flask", "run", "--host=0.0.0.0"]