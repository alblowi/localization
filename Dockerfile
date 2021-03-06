FROM ubuntu:16.04
MAINTAINER Sint
#UPDATE
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get upgrade -y

# INSTALL SUPERVISOR
RUN apt-get install -y supervisor && \
    mkdir -p /var/log/supervisor && \
    supervisord --version
ADD configs/supervisor/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# INSTALL Apache2
ADD configs/apache2/apache2-service.sh /apache2-service.sh
RUN apt-get install -y apache2 && \
    chmod +x /*.sh && \
    a2enmod rewrite
ADD configs/apache2/apache_default /etc/apache2/sites-available/000-default.conf
ADD configs/apache2/supervisor.conf /etc/supervisor/conf.d/apache2.conf

#INSTALL APACHE AUTO-ALIAS
COPY configs/domain_configs /domain_configs
COPY configs/autoload_aliases.sh /autoload_aliases.sh
RUN chmod +x /autoload_aliases.sh

#INSTALL GIT
RUN apt-get install -y software-properties-common wget \
    git && \
    git --version

#INSTALL COMPOSER
ENV COMPOSER_HOME /root/.composer
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer \
    --install-dir=/usr/bin --version=1.0.0-alpha10
RUN composer --version

#INSTALL PYTHON
RUN apt-get install -y python python3 python-pil pylint && \
    python --version && \
    python3 --version


#INSTALL ADDONS NODE
COPY configs/node/install_phantomjs.sh /install_phantomjs.sh
RUN chmod +x /install_phantomjs.sh
RUN bash /install_phantomjs.sh

COPY configs/node/dependencies.sh /usr/bin/npm_dependencies
RUN chmod +x /usr/bin/npm_dependencies


#INSTALL MONGO DRIVER 3
COPY configs/mongo/mongo_driver.sh /mongo_driver.sh

RUN chmod +x /mongo_driver.sh
RUN bash /mongo_driver.sh

#INSTALL MONITOR FILES
COPY configs/monitor.sh /monitor.sh
RUN chmod +x /monitor.sh
RUN mv monitor.sh /usr/local/bin/monitor

#SET ServerName
RUN echo "ServerName 'localhost'" >> /etc/apache2/apache2.conf

#CLEAN
RUN apt-get clean && apt-get autoremove

#SET TERMINAL
ENV TERM xterm
CMD bash /autoload_aliases.sh && supervisord
VOLUME /var/www/html
WORKDIR /var/www
EXPOSE 22 80 27017 27018
