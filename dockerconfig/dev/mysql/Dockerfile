FROM mysql:5.7.27


ENV AUTHOR zhp@602013597

RUN  rm  /etc/localtime

#COPY dockerconfig/localtime /etc/localtime

COPY dockerconfig/Shanghai /etc/localtime
RUN  echo 'Asia/Shanghai' >/etc/timezone
