# create -> Post 
# read  -> get
# update -> put
# delete -> Delete
# uvicorn main:app --reload    run command
from fastapi import FastAPI
from functions import intrest
from fastapi.middleware.cors import CORSMiddleware

# class User(BaseModel):
#     name: str
#     surname: str
#     age: int
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



# @app.get("/divide")
# def handle_divide(a: float, b: float, response: Response):
#     return divide(a, b, response)

# @app.post("/getUser")
# def handle_getUser(data: User):
#     return getUser(data)

# # Quuery
# @app.get("/hello")
# def handle_hello(name: str, surname: str, age: int):
#     return hello(name, surname, age)

# # # Paramme
# @app.get("/goodbye/{name}/{age}")
# def handle_goodbye(name: str, age: int):
#     return sayGoodbye(name, age)
      
# # Simple intrest Calculate
@app.get("/interest")
def handle_intrest(principle: int, r:int, n: int):
    return intrest(principle, r, n)
    


# # # 200 -> Ok
# # # 201 -> Created
# # # 400 -> bad request
# # # 403 -> Forbidden
# # # 404 -> not found
# # # 500 -> Internal Server Error    







# # #     } # http://127.0.0.1:8000/interest?principle=6500000&r=8&n=10










# # # # uvicorn main:app --reload
# # # # http://127.0.0.1:8000/hello?name=Om&surname=Modi?age=22
# # # # http://127.0.0.1:8000//Goodbye/Om/22
