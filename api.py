import asyncio
import io
import os
import ai
import metaphysic
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
from logging.config import dictConfig
import log_config
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI 
from fastapi.middleware.trustedhost import TrustedHostMiddleware

dictConfig(log_config.logger)


class AboutMe(BaseModel):
    physical: str
    ending: str

frontend_domain = "https://borndate.web.app/"
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[frontend_domain],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=[frontend_domain] 
)

@app.get("/")
def read_root():
    return {"Server": "Running"}


@app.get("/result/{dob}")
async def read_dob(dob: str):
    input_array = list(map(str, dob))
    if dob[4:8] == "2000":
        input_array[4:8] = list("2005")
    image_name = metaphysic.begin_drawing(dob, input_array, True)
    buffer = io.BytesIO()
    img = Image.open(image_name)
    img.save(buffer, format="PNG")
    cleanUpFile(image_name)
    return Response(content=buffer.getvalue(), media_type="image/png")


@app.get("/element/{dob}")
async def get_dominant_element(dob: str):
    [dominant_dict, physical, spirit, ending] = metaphysic.analysis(dob)
    element_list = []
    for key, value in dominant_dict.items():
        element = key
        count = value
        element_list.append(metaphysic.get_element_analysis(element, count))
    element_list = sorted(element_list,key=lambda element: element['count'], reverse=True)

    analyze_element_object = {
        'physical': physical,
        'spirit': spirit,
        'ending': ending,
        'elements': element_list
    }

    return JSONResponse(content=analyze_element_object)


def cleanUpFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")


@app.post("/aboutMe/")
async def get_about_self(aboutMe: AboutMe):
    [response, error] = await asyncio.get_event_loop().run_in_executor(None, ai.getAboutMe, aboutMe.physical, aboutMe.ending)
    if response is None:
        raise HTTPException(status_code=404, detail=error)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)