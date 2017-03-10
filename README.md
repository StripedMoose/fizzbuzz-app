# FizzBuzz API Server
A quick and dirty python/flask app to play a variation
of the [fizzbuzz game](https://en.wikipedia.org/wiki/Fizz_buzz).

## API Reference
### /ping
Test server response

### /query/$int
Query server for approprate fizzbuzz reply. Server returns json-formatted string with ${int}+1, "fizz", "buzz", or "fizzbuzz" as appropriate

## Docker Integration

### Building the container

```docker build -t fizzbuzz:latest .```

### Running the container

Via docker:

```docker run -d -p 5000:5000 fizzbuzz```

via docker-compose:

```docker-compose up```

### Querying the server
When run via the container, the server will be available at: 

```http://localhost:5000```
