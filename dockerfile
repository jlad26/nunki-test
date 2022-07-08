FROM continuumio/miniconda3

WORKDIR /app

LABEL maintainer="Jon Anwyl <jon.anwyl@gmail.com>"

# Only required for module style execution.
ENV FLASK_APP=nunki-test-api.py

# Create the environment.
COPY environment.yml .
RUN conda update conda -y && conda env create -n nunki -f environment.yml

# Define the port number the container should expose.
EXPOSE 5000

COPY app .

# ENTRYPOINT for module style execution.
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "nunki", "python3", "-m", "flask", "run", "--host=0.0.0.0"]

# ENTRYPOINT for script style execution.
# ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "nunki", "python3", "nunki-test-api.py"]