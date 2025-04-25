from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
import models
from database import session
from pydantic import BaseModel
import game_logic


router = APIRouter()   #fast api app


def get_db():         #creating a database session
    db = session()
    try:
        yield db
    finally:
        db.close()


class UserSchema(BaseModel):    #model for validation and serialization of data received from fast api json format
    username: str
    password: str
    email: str

class GuessSchema(BaseModel):  
    username: str 
    guess: int



@router.post('/register')  #register endpoint
async def register(user:UserSchema , db: Session = Depends(get_db)):

    exists = db.query(models.Users).filter(models.Users.username==user.username).first()

    if(exists):
        raise HTTPException(status_code = 400,detail = "User already exists...")

    new_user = models.Users(username = user.username,password = user.password,email = user.email,free_game = 5)

    db.add(new_user)
    db.commit()
    return {"message": "User registered..."}


@router.post('/play')
async def play(guess: GuessSchema, db: Session = Depends(get_db)):

    exist = db.query(models.Users).filter(models.Users.username==guess.username).first()

    if not exist:
        raise HTTPException(status_code = 404, detail = "User not found...")
    if exist.free_game <=0:
        raise HTTPException(status_code = 403 ,detail = "No more free chances left...")
    result = game_logic.guess(guess.guess)
    exist.free_game -=1
    db.commit()
    return {"correct": result["correct"],
            "games left": exist.free_game,
            "status": result["status"]}

    



