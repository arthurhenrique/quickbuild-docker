FROM java:openjdk-7u65-jdk
# maintainers details
# system installations
RUN apt-get update && apt-get install -y wget 
# product installations
RUN wget 'https://build.pmease.com/download/4649/artifacts/quickbuild-8.0.26.tar.gz' -O quickbuild.tar && tar -zxvf quickbuild.tar -C /opt 
# Expose the default QB port
EXPOSE 8810
# start quickbuild
ENTRYPOINT /opt/quickbuild-8.0.26/bin/server.sh console
