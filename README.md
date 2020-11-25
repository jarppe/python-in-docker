# Example setup for Python in Docker

Example setup for creating Docker containers for
Python development.

## Minimal

The folder `minimal` contains a minimal Python HTTP server
that responds to all `GET` requests with plain text response
`Hello world`. The server listens on `0.0.0.0:8080`.

Build docker image:

```bash
cd minimal
docker build -t python-in-docker:minimal .
```

```bash
docker run --init --rm -p 8080:8080 python-in-docker:minimal
```

```bash
$ http :8080
HTTP/1.0 200 OK
Content-type: text/html
Date: Wed, 25 Nov 2020 18:47:04 GMT
Server: BaseHTTP/0.6 Python/3.10.0a2

Hello world
```

## Using 3rd party libraries

The folder `fastapi` contains a similar HTTP server, but
this uses [FastAPI](https://fastapi.tiangolo.com/) and
[uvicorn](https://www.uvicorn.org/) libraries.

Build:

```bash
cd fastapi
docker build -t python-in-docker:fastapi .
```

```bash
docker run --init --rm -p 8080:8080 python-in-docker:fastapi
```

```bash
$ http :8080
HTTP/1.1 200 OK
content-length: 25
content-type: application/json
date: Wed, 25 Nov 2020 18:49:35 GMT
server: uvicorn

{
    "message": "Hello World"
}
```

## Using docker for Python development

In my opinion the best way to develop in Python (or in any other
language for that matter) is to do all your development inside
a Docker container. The folder `dev` has the previous FastAPI
example, but with one minor difference: the `uvicorn` server
is started with `--reload` flag.

Build:

```bash
cd dev
docker build -t python-in-docker:dev .
```

```bash
docker run --init --rm -p 8080:8080 -w /app -v $(pwd):/app python-in-docker:dev
```

```bash
$ http :8080
HTTP/1.1 200 OK
content-length: 25
content-type: application/json
date: Wed, 25 Nov 2020 18:49:35 GMT
server: uvicorn

{
    "message": "Hello World"
}
```

Let the container run and open the `server.py` file on editor. Change
the response message and save the file. Notice how `uvicorn` detected the change and reloaded the application. Try the HTTP API again:

```bash
$ http :8080
HTTP/1.1 200 OK
content-length: 48
content-type: application/json
date: Wed, 25 Nov 2020 18:56:33 GMT
server: uvicorn

{
    "message": "Could 2020 be over already, please"
}
```

## TODO

* Explain docker command flags
* Explain why requirements are installed before sources are copied
* Explain how to publish and share images
* Explain build stages
* Explain why dev-in-docker is 2nd best way to develop
* Explain how to debug, i.e. exec into container etc
* Add pointers to docker installation
* Windows support, i.e. change the `$(pwd)` to something windows understands
* Write a blog about all this
