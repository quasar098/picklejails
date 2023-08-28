FROM python:3.9 AS app

FROM pwn.red/jail
COPY --from=app / /srv
RUN mkdir /srv/app
COPY run.sh /srv/app/run
COPY flag.txt /srv/app/flag.txt
COPY jail.py /srv/app/jail.py
RUN chmod +x /srv/app/run
ENV JAIL_MEM=24M JAIL_CONNS_PER_IP=8 JAIL_PIDS=8 JAIL_CPU=100 JAIL_TIME=30