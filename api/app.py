import os
import pandas as pd
from fastapi import FastAPI


app = FastAPI()

coup_de_pouce = "👍👍👍👍👍👍👍👍"


@app.get("/")
def root():
    """Root endpoint returning a coup de pouce"""
    return {"wsh" : coup_de_pouce}
