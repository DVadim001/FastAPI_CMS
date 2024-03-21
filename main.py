from fastapi import FastAPI
from users.user_api import user_router
from content.content_api import content_router
from sites.site_api import site_router
from database import Base, engine

app = FastAPI(
    title="CRM",
    docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(content_router)
app.include_router(site_router)
