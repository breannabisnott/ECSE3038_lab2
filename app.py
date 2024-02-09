from fastapi import FastAPI, Request

app = FastAPI()

data = []

@app.post("/person")
async def post_person(request: Request):
    person = await request.json()
    data.append(person)

    check = all(data)
    
    # for info in person:
    #     if len(info["name"]) == 0:
    #         check == False
    
    if check == False:
        result = {"error_message": "invalid request"}
    else:
        result = data
    
    return {
        "success": check,
        "result": result
    }

@app.get("/person")
def get_person():
    return data