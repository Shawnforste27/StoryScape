from fastapi import FastAPI

from core.config import settings
from routers import story, job
from db.database import create_tables



create_tables()

app = FastAPI(
    title="StoryScape",
    description="api to generate cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)



# app.include_router(story.router, prefix=settings.API_PREFIX)
# app.include_router(job.router, prefix=settings.API_PREFIX)


app.include_router(story.router, prefix=("/api"))
app.include_router(job.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)