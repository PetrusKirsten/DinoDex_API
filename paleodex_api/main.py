from fastapi import FastAPI

from paleodex_api.routers import api_router

app = FastAPI(
    title       = "PaleoDex API", 
    description = "API for accessing dinosaur data",
    version     = "1.0.0"
)

app.include_router(api_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', 
                host        = '0.0.0.0',
                port        = 8000,
                reload      = True, 
                contact     = {
                    "name"  :"Petrus Kirsten",
                    "email" :"petrus.kirsten@gmail.com"
                },
                log_level   = 'info',
                docs_url    = "/docs",
                redoc_url   = "/redoc",
                openapi_url = "/openapi.json",
    )
