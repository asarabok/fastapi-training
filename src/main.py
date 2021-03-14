from fastapi import FastAPI, Depends
from .schemas import TeamSchema
from sqlalchemy.orm import Session
from .database import get_db
from .models import Player, Team


app = FastAPI()


@app.post("/teams")
def create(details: TeamSchema, db: Session = Depends(get_db)):
    team = Team(**dict(details))
    db.add(team)
    db.commit()

    return {
        "success": True,
        "created_id": team.id
    }
