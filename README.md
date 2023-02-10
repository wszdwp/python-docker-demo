# python-docker-demo
python-docker-demo

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
