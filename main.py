from fastapi import FastAPI
import uvicorn
from gcpconn import topFivePosts
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/topfive", response_class=PlainTextResponse)
async def topfive():
    """Print the top five ranking stackoverflow posts"""

    result = topFivePosts()
    print(result)
    # return {result.to_json(orient='table')}
    return result.to_string()


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
