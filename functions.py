from fastapi import Response
from pydantic import BaseModel


# class User(BaseModel):
#     name: str
#     surname: str
#     age: int

# def divide(a: float, b: float, response: Response):
#     try:
#         result = a / b
#         response.status_code = 200
#         return {
#             "isSucess" : True,
#             "result" : result
#     }
#     except Exception as e:
#         response.status_code = 500
#         return {
#             "isSucess" : False,
#             "message" : str(e)
#         }


    
# def getUser(data: User):
#     try:
#         print(data)
#         return{
#           "isSucess" : True,
#           "name" : data.name,
#           "surname" : data.surname,
#           "age" : data.age
#     }
#     except Exception as e:
#             return{
#                 "isSuccess" : False,
#                 "message" : str(e)
#             }
    
            
# def hello(name: str, surname: str, age: int):
#     try:
#         return {
#             "isSucess" : True,
#             "message": f"Hello, {name} {surname} {age}!"
#                 }
#     except Exception as e:
#         return {"isSucess" : False,"message": str(e)}


# sayHello = hello
    
# def sayGoodbye(name: str, age: int):
#     try:
#         return {"isSucess" : True,"message": f"Goodbye, {name} {age}!"}
#     except Exception as e:
#         return {"isSucess" : False,"message": str(e)}  
    
def intrest(principle: int, r:int, n: int):
    try:
        return {
            "isSucess" : True,
            "principle" : principle,
            "si" : (principle*r*n)/100,
            "totalPayment" : principle + (principle*r*n)/100
        }
    except Exception as e:
        return {"isSucess" : False,"message": str(e)}


si = intrest