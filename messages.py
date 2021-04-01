STATUS = "STATUS"
OK = "OK"
FAILED = "Failed"
MESSAGE = "MESSAGE"
SUCCESS = "Success"
ERROR = "Error"
registeredEventsSchema = {
    "type": "object",
    "properties": {
        "pid": {"type": "string"}        
    },
    "required": ["pid"]
}
SWAGGER_URL = '/api/docs'  
API_URL = "/static/swagger.yaml"
