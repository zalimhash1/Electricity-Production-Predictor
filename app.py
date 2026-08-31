from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from pydantic import BaseModel,Field,field_validator
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware


with open("pipe.pkl", 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500",
                   "https://electricity-production-predictor-1.onrender.com"],
    allow_methods=["*"],
    allow_headers=["*"]
)

countries = ['Australia', 'Austria', 'Canada', 'Czech Republic', 'Denmark',
       'Germany', 'New Zealand', 'OECD Asia Oceania', 'OECD Europe',
       'Poland', 'Republic of Turkiye', 'Slovenia', 'Spain', 'Belgium',
       'Finland', 'Greece', 'IEA Total', 'Iceland', 'Japan',
       'Netherlands', 'Norway', 'OECD Americas', 'Portugal',
       'Slovak Republic', 'Sweden', 'United States', 'Estonia', 'Ireland',
       'Korea', 'OECD Total', 'Switzerland', 'Chile', 'Italy', 'Latvia',
       'Lithuania', 'Luxembourg', 'Mexico', 'France', 'Hungary',
       'United Kingdom', 'Colombia', 'Malta', 'Serbia', 'Bulgaria',
       'Cyprus', 'North Macedonia', 'Romania', 'Brazil', 'India',
       'Croatia', 'Argentina', 'Costa Rica']

products = ['Final consumption', 'Low carbon', 'Wind', 'Not specified',
       'Non-renewables', 'Oil', 'Total imports', 'Electricity supplied',
       'Coal', 'Total exports', 'Fossil fuels', 'Distribution losses',
       'Other renewables aggregated', 'Hydro', 'Electricity trade',
       'Renewables', 'Used for pumped storage', 'Solar', 'Geothermal',
       'Total combustible fuels', 'Other combustible non-renewables',
       'Combustible renewables', 'Net electricity production',
       'Natural gas', 'Others', 'Nuclear', 'Other renewables']

class UserInput(BaseModel):

    COUNTRY: Annotated[str, Field(..., max_length=18, description="Enter the country name")]
    YEAR: Annotated[int, Field(..., gt=2009,lt=2023, description='Give the year')]
    MONTH: Annotated[int, Field(..., ge=1,le=12, description='Mentioned the month')]
    PRODUCT: Annotated[str, Field(..., max_length=40,description='Tell me required product')]

    @field_validator('COUNTRY')
    @classmethod
    def transform_country(cls,value):
        clean_value = value.strip().lower()
        for country in countries:
            if country.lower() == clean_value:
                return country
        raise ValueError('Country not found')
        
    @field_validator('PRODUCT')
    @classmethod
    def transform_product(cls,value):
        product_value = value.strip().lower()
        for product in products:
            if product.lower() == product_value:
                return product
        raise ValueError('Product not found')


@app.get('/')
def hello():
    return {'message':'Electricity Production API'}

@app.get("/about")
def about():
    return {'message':'This is the prediction of Electricity production'}

@app.post('/predict')
def predict_check(data:UserInput):
    input_df = pd.DataFrame([{
        'COUNTRY':data.COUNTRY,
        'YEAR':data.YEAR,
        'MONTH': data.MONTH,
        'PRODUCT': data.PRODUCT
    }])
    try:
        prediction = float(model.predict(input_df)[0])
        return JSONResponse(status_code=200, content={"predicted_value":prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})