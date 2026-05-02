import asyncio
import ai
import metaphysic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from logging.config import dictConfig
import log_config

dictConfig(log_config.logger)


class AboutMe(BaseModel):
    physical: str
    ending: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Server": "Running"}



@app.get("/element/{dob}")
async def get_dominant_element(dob: str):
    if not metaphysic.check_input(dob):
        raise HTTPException(status_code=400, detail="DOB must be in ddmmyyyy format.")
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


@app.get("/analysis/{dob}")
async def get_analysis(dob: str):
    if not metaphysic.check_input(dob):
        raise HTTPException(status_code=400, detail="DOB must be in ddmmyyyy format.")
    return JSONResponse(content=metaphysic.build_analysis_response(dob))


@app.get("/compatibility/{first_dob}/{second_dob}")
async def get_compatibility(first_dob: str, second_dob: str):
    if not metaphysic.check_input(first_dob) or not metaphysic.check_input(second_dob):
        raise HTTPException(status_code=400, detail="DOB must be in ddmmyyyy format.")
    return JSONResponse(content=metaphysic.build_compatibility_response(first_dob, second_dob))




@app.post("/aboutMe/")
async def get_about_self(aboutMe: AboutMe):
    [response, error] = await asyncio.get_event_loop().run_in_executor(None, ai.getAboutMe, aboutMe.physical, aboutMe.ending)
    if response is None:
        raise HTTPException(status_code=404, detail=error)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
