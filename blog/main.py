from fastapi import FastAPI
from . import schemas


app = FastAPI()



@app.post('/newblog')
def create(req: schemas.Blog):
    return {
        "title": req.title,
        "content": req.content,
        "tags": req.tags,
        "published_by": req.published_by
    }
