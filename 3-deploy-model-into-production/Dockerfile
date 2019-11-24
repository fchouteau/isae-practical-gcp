FROM python:3.7

# Install pytorch
RUN pip install torch==1.3.1 torchvision==0.4.2
# Install additionnal requirements
RUN pip install gunicorn flask Pillow

# Install application
COPY app.py /app/
COPY gunicorn.conf.py /app/
COPY index_to_classes.json /app/

# Set workdir
WORKDIR /app/

# Launch web application
ENV PYTHONPATH=/app
EXPOSE 8080
ENTRYPOINT ["gunicorn", "--log-level", "INFO", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:8080", "app:APP"]
