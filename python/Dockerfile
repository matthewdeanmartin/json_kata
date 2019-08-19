FROM python:3.7.4-alpine3.9
COPY simple_calls simple_calls
COPY Pipfile Pipfile
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python3", "-m", "simple_calls"]