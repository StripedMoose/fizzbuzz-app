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
When run via the container, the server will be available on [http://localhost:5000](http://localhost:5000)


## Deploying to AWS API Gateway / Lambda
Fizzbuzz App uses a tool called [Zappa](https://github.com/Miserlou/Zappa#basic-usage) to take care of serverless deployments.

### Setup
Zappa must be run in an virtualenv, so fire it up:

```
virtualenv fizzbuzz
source fizzbuzz/bin/activate
pip install -r requirements.txt
```

Then add a profile to the zappa_settings.json file:

```
"${zappa_profile}": {
	"app_function": "src.fizzbuzz.app", 
	"s3_bucket": "${s3_bucket_name}",
	"memory_size": 128,
	"profile_name": "${aws_profile}"
}
```

`${zappa_profile}` is the name you'll call this deployment (usually "dev", "prod", etc)

`${s3_bucket}` is the name of a new or exiting bucket into which zappa can drop the deployment

`${aws_profile}` is the profile from your ~/.aws/credentials 

### Deploying
Simply call

```zappa deploy ${zappa_profile}```

and zappa will cake care of everything, handing you back an endpoint when it complete.

### Status & Monitoring
`zappa status`

`zappa tail ${zappa_profile}`

## Deploying to AWS EC2 w/ELB
For a more traiditonal deployment, there is a clouformation template "fizzbuzz-ec2.yml" provided with the distribution.  

Running this tempate will create the following:

* A Cloudformation stack with all resources required for the service
* Elastic Load Balancer configured to serve port 5000
* Autoscaling Group with CPU load based scale up & scale down policies
* A single EC2 instance with the latest version of this code running on port 5000
* Secrutity groups and IAM roles for the resources

### Deploying
Simply upload this file to AWS Cloudformation. The aws CLI doesn't seem to support YAML template yet, so for testing this has been done via the AWS Console.

### Verification
Once the stack is up, gather the public DNS entry for the load balancer and test:

```
curl http://${elb_endpoint}/ping

curl http://${elb_endpoint}/query/${int}
```


