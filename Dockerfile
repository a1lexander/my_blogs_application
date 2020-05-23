# Pull base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory - чтобы не указывать длинный путь -
# все команды будут выполняться из этого каталога
WORKDIR /code

# Install dependencies, --system - означает, что наши пакеты доступны во всем docker
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
