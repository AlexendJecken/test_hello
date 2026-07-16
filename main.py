from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="FastAPI Hello for Render")

@app.get("/")
def read_root():
    """
    Returns a JSON object with a Hello message.
    """
    return {"message": "Hello"}

@app.get("/hello")
def say_hello():
    """
    Returns a plain text 'Hello' response.
    """
    return PlainTextResponse("Hello")

@app.get("/health")
def health_check():
    """
    Health check endpoint for Render.
    """
    return {"status": "healthy"}
