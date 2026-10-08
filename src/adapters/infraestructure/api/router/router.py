from fastapi import APIRouter
from ....input import CreateMessage;

test_postman = APIRouter(
    prefix="/test_postman",
    tags=["/test_postman"],
    responses={404: {"description": "No encontrado"}},
)

@test_postman.post("/message")
async def message_post(message:dict): 
    new_message = CreateMessage(); 
    print(message); 
    return {"message": "Lista de usuarios"}; 