FROM tensorflow/tensorflow:latest


COPY ./requirements.txt /NLPRecommendWeb/webapp/requirements.txt

WORKDIR /NLPRecommendWeb/webapp

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["run.py"]