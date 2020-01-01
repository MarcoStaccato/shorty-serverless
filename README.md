# AWS


## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)

## Setup process

```
sam build
```

### Local development

**Invoking function locally using a local sample payload**

```bash
sam local invoke UploadRequestFunction --event event.json
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```
