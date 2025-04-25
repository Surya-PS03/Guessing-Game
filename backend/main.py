from fastapi import FastAPI
import models
from database import engine
from Router.guess_game import router


app = FastAPI()

print("Creating the db....")
models.base.metadata.create_all(bind=engine)
print("Done.")

app.include_router(router)


    



