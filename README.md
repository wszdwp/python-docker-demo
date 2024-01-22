# python-docker-demo
![github action](https://github.com/wszdwp/python-docker-demo/actions/workflows/main.yml/badge.svg)

## Guide
https://docs.docker.com/language/python/build-images/

## Docker hub repos
https://hub.docker.com/repositories

## Run  
```
cd /path/to/python-docker
python3 -m venv .venv
source .venv/bin/activate
(.venv) $ python3 -m pip install Flask
(.venv) $ python3 -m pip freeze > requirements.txt
(.venv) $ python3 -m flask run
```

```
(.venv) $ python3 -m pip install -r requirements.txt
(.venv) $ python3 -m flask --debug run
```

```
docker run --publish 8000:5000 python-docker
```

## MongoDB on MacOS
To run MongoDB (i.e. the mongod process) manually as a background process, 

**run**
```
mongod --config /usr/local/etc/mongod.conf --fork
```

**connect**
```
mongosh
```

**stop**
```
To stop a mongod running as a background process, connect to the mongod using 
mongosh, and issue the shutdown command as needed.
```


## VENV
print site-packages path
```
python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
```
