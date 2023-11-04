FROM python:3.9-bullseye

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict-flask.py", "randomforest.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "python" ]

CMD [ "predict-flask.py" ]