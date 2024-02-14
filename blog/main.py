from fastapi import Depends, FastAPI, HTTPException,status, Response
from sqlalchemy.orm import Session
from . import models,schemas
from .database import SessionLocal, engine



models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()


@app.get("/")
def send():
    return "Hello There!, this is  Anurag's Blogging Website"



@app.post('/newblog',status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog,db:Session= Depends(get_db)):
    new_blog =  models.Blog(title= req.title, body=req.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog



@app.get('/blogs')
def allblogs(res:Response, db:Session= Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



@app.get('/blog/{id}',status_code=200)
def getBlog(res:Response,id,db:Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,detail=f"The blog with the id = {id} not found")
    
    return blog


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id,req: schemas.Blog,db:Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    print(blog)
    print(id)
    db.query(models.Blog).filter(models.Blog.id == id).update(
        {
            models.Blog.title:req.title,
            models.Blog.body:req.content,
        }
    )
    
    return "Update Successful"
    


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(res:Response,id,db:Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "blog deleted Sucessfully"
