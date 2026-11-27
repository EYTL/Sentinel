# demo_service/Dockerfile (PHASE 1)
#
# Write the steps to package demo_service as a container. You have already seen
# one in your EMS project: look at EMS/Dockerfile for the shape. You need:
#   1. a base image with Python           (FROM python:3.11-slim)
#   2. a working folder inside the image  (WORKDIR)
#   3. install Flask                      (COPY a requirements file, then RUN pip install)
#   4. copy app.py in                     (COPY)
#   5. say which port it uses             (EXPOSE 5000)
#   6. the command that starts the app    (CMD)
#
# Then, from the sentinel folder, you will:
#   docker build -t demo-service ./demo_service
#   docker run -d --name demo-service -p 5000:5000 demo-service
# The container name MUST be "demo-service": config.yaml refers to it.
#
# PROOF: `docker ps` lists it, and http://localhost:5000/health answers.
