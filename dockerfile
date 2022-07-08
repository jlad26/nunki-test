FROM continuumio/miniconda3

WORKDIR /app

LABEL maintainer="Jon Anwyl <jon.anwyl@gmail.com>"

# Create the environment.
COPY environment.yml .
RUN conda update conda -y && conda env create -n nunki -f environment.yml

# define the port number the container should expose
EXPOSE 5000

COPY app .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "nunki", "python3", "nunki-test-api.py"]