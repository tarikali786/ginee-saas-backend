FROM consultrajs/ginee-docker:BaseBackendv1
# setup environment variable 
USER docker

ENV DockerHOME=/home/docker/data/app 

# RUN sudo chmod -R 777 /root

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
# RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  



RUN pip install -r requirements.txt  


COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
