# Lakbay.ph

#### Dependencies
Python 3
Pip
Pandas
Requests
Uvicorn
FastAPI

$ pip install pandas requests uvicorn[standard] fastapi pydantic starlette typing datetime

#### Start the service
$ uvicorn main:app --reload

##### Testing Guide

##### Mobile App Endpoint
```javascript
class Rating(BaseModel):
	name: str = None
	city: Dict[str,str]
	ownerId: str
	ratingRange: int = None
	attractionTags: Dict[str,str] = None
	hotelTags: Dict[str,str] = None
	status_tours: str = None
	status_restos: str = None
	status_hotels: str = None
```
##### Expected JSONResponse on Database
```javascript
{
	"travelplan": {
		"user_id": {
			"plan_1" : {
				"tours": {
					"name": str,
					"location": str,
					"address": str,
					"tags": str,
					"ratings": float
				},
				"resto": {
					"name": str,
					"location": str,
					"address": str,
					"type": str,
					"ratings": float
				},
				"hotel": {
					"name": str,
					"location": str,
					"address": str,
					"ratings": float,
					"class": float
				},
				"tours_status": str,
				"restos_status" str,
				"hotels_status" str
			}
		}
	}
}
```
