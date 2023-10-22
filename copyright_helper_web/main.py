
"""
uvicorn copyright_helper_web.main:app --host 0.0.0.0 --port 8080
"""
import os
import uvicorn
# from fastapi import Depends, FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
from copyright_helper_web.routers import code2doc

app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

root = os.path.abspath(os.path.join(os.path.basename(__file__), ".."))
print(root)
# try:
#     # 这里在部署的时候，路径总是错，暂不知为何，所以部署的时候改成绝对路径
#     # app.mount("/static", StaticFiles(directory=f"{root}/static"), name="static")
#     app.mount("/static", StaticFiles(directory=f"/home/smit/PycharmProjects/copyrighthelper/copyright_helper_web/static"), name="static")
# except RuntimeError as e:
#     # unittest error sometimes
#     print(e)
#
#
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        # swagger_js_url="/static/swagger-ui-bundle.js",
        # swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

app.include_router(
    code2doc.router,
    prefix="/api/v1",
    tags=["软件著作权代码生成接口"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}},
    # deprecated=True,
)

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8080)