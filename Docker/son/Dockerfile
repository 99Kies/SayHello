FROM debian/python:3

RUN git clone https://github.com/99kies/sayhello && \
    cd /sayhello && \
    pip install -r piplist.txt && \
    export FLASK_APP=/sayhello/sayhello && \
    flask forge

ENV FLASK_APP=/sayhello/sayhello

