# AWS


## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)

## Setup process

**Make sure to have docker running before**

```
sam build --use-container --skip-pull-image
```

### Local development

**Invoking function locally using a local sample payload**

```bash
sam local invoke ShortyFunction --event events/get-event.json
sam local invoke ShortyFunction --event events/post-event.json
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```
**call the function with**
```bash
curl -XGET -d '{"hash": "oqchgDn"}' http://localhost:3000/shorty -v
```