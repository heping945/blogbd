FROM heping945/redis

#
ENV AUTHOR zhp@602013597
#
#
#COPY dockerconfig/localtime /etc/localtime

#RUN cd /etc && mkdir timezone


COPY dockerconfig/Shanghai /etc/localtime
RUN  echo 'Asia/Shanghai' >/etc/timezone