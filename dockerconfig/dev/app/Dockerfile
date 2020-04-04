FROM heping945/python36

ENV PYTHONUNBUFFERED 1
ENV AUTHOR zhp@602013597

WORKDIR /app

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

#RUN  rm  /etc/localtime
#COPY dockerconfig/localtime /etc/localtime

COPY dockerconfig/Shanghai /etc/localtime
RUN  echo 'Asia/Shanghai' >/etc/timezone

RUN pip install /src/xadmin-master.zip -i https://pypi.douban.com/simple

RUN pipenv install --system --ignore-pipfile



COPY dockerconfig/dev/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
