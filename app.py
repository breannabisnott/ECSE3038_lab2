from fastapi import FastAPI, Request

app = FastAPI()

data = []

@app.post("/person")
async def post_person(request: Request):   
    person = await request.json()
    data.append(person)

    check = True

    list = person.values()
    for value in list:
        if value == '':
            check = False
    
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