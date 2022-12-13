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

@app.get("/calc/{num1}/{operation}/{num2}")
async def calc(num1: int, operation: str, num2: int):
    """Simple calculation between 2 variables"""
    
    if operation != '+' and operation != '-' and operation != '*' and operation != 'd':
        return {"Wrong operation input"}

    elif operation == '+':
        total = num1 + num2
        return {"total": total}
    
    elif operation == "-":
        total = num1 - num2
        return {"total": total}

    elif operation == "*":
        total = num1 * num2
        return {"total": total}

    elif operation == "d":
        if num2 == 0:
            return {"The divisor cannot be zero"}
        else:
            total = num1/num2
            return {"total": total}
    


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
