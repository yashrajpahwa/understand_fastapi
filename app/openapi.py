from fastapi.openapi.utils import get_openapi


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description="Demo API that walks from basics to advanced FastAPI features.",
        routes=app.routes,
        tags=[
            {"name": "basic", "description": "Hello world, background tasks, errors"},
            {"name": "auth", "description": "API key and OAuth2 password flow"},
            {"name": "users", "description": "User registration and listing"},
            {"name": "items", "description": "Async DB, pagination, caching"},
            {"name": "websockets", "description": "WebSocket echo"},
        ],
    )
    schema["info"]["x-demo"] = "feature-tour"
    app.openapi_schema = schema
    return schema
