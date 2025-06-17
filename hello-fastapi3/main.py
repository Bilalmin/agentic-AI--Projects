from fastapi import FastAPI,Path,Query


app = FastAPI() 

#path parameters

@app.post("/name/{username}/{user_id}")
def dyn_root(username: str, user_id: int=Path(..., gt=0, lt=100)):
    return {"username": username,"user_id": user_id}

#simlple routing

@app.get("/name/bilal")   
def root():
    return {"name": "bilal amin"}

#query parameters

@app.get("/users/all")
def get_all_users(limit: int | None = Query(..., gt=0, lt=100)):
    print(f"Limit is {limit}") 
    if limit:
        return {"users": "ali amin"}
    else:
        return {"users": ["ali amin", "bilal amin", "ahmed amin"]}
    # return {"users": ["ali amin", "bilal amin", "ahmed amin"]}
    # return {"users":[ "ali amin", "bilal amin", "ahmed amin"]}