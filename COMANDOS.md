
## DOCKER

´´´
docker run nginx
´´´

First, It pulled the image and saved it locally, then it put that image inside of the running-time enviroment, AKA a container, and it made it run. 


TIPS

> 1.
 
 ``` 
 docker run --name erhpepe
 ```

 name the containers with the name-tag. This helps to keep organized, If not docker will assign names randomly to your containers.
 
> 2. Versión
 ```
    docker pull [OPTIONS] NAME [:TAG|@DIGEST]
 ```


```
docker ps 
```

```
docker ps -a
```
Running containers names and **id**s.

 
## START AND STOP 

```
 docker stop id
```
Stop running the container 

```
 docker start id
```
Start running the container 

## Networking in docker, -p tag 
Docker is a "virtual machine" of sorts and  has its own internal network for its containers.

<center>

![!!!](./images/Port!.png)
</center>

They have to **map** those ports **manually** host manually If you want them to be **accesible from the host's network**.

To do this, add the port tag to your command when you deploy a container. 

Then list the hosts port, and then docker port.
```
docker run myapp:2.0 -p 8080:80
```
> 8080:80
    Host port:docker port.

When running multiple containers from one host, be sure to run different containers on separate containers on the host. 

```
docker network ls
```

```
docker inspect --name
```
To see more info on that network. 


## DOCKER KILL
```
docker kill --name
```

```
docker kill --id
```

Stop and kill does not remove the containers or the image from your host machine, it just stops the containers function. 

## Docker images and docker rmi

```
docker rm --name
```
These delete the container, but the docker image is still stored locally.















































