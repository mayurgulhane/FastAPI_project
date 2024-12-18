from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db:Session, author_id=1):
    blog = Blog(
        title = blog.title,
        slug = blog.slug,
        content = blog.content,
        author_id = author_id   
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog