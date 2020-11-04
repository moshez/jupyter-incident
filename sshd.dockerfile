FROM debian
ARG sshkey

RUN apt-get update
RUN apt-get install -y --no-install-recommends openssh-server

RUN mkdir -p /var/run/sshd /root/.ssh
RUN chmod 700 /root/.ssh
RUN echo "$sshkey" > /root/.ssh/authorized_keys

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
