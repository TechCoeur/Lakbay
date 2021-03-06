# Lakbay.ph :trollface::trollface::trollface:

#### Dependencies
Python 3
Pip
Pandas
Requests
Uvicorn
FastAPI

```
$ pip install pandas requests uvicorn[standard] fastapi pydantic starlette typing datetime
```

#### Start the service
```
$ uvicorn main:app --reload
```

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
##### Expected JSONResponse on Firebase Realtime Database
https://lakbayph-88c82.firebaseio.com/
```javascript
{
	"preferences": {
		"user_id": str {
			"city": {
				"id": int,
				"name": str
			}
			"ownerId": str,
			"ratingRange": int
		}
	}
}		
{
	"travelplan": {
		"user_id": str {
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
				"restos_status": str,
				"hotels_status": str
			}
		}
	}
}
```
*not used parents for recommender:  "mostbooked", "orders", "products", "travelplans"

#### FastAPI Request samples
```javascript
{
  "name": "string",
  "city": {
    "property1": "string",
    "property2": "string"
  },
  "ownerId": "string",
  "ratingRange": 0,
  "attractionTags": {
    "property1": "string",
    "property2": "string"
  },
  "hotelTags": {
    "property1": "string",
    "property2": "string"
  },
  "status_tours": "string",
  "status_restos": "string",
  "status_hotels": "string"
}
```

#### Response samples
```javascript
{
  "name": "string",
  "city": {
    "property1": "string",
    "property2": "string"
  },
  "ownerId": "string",
  "ratingRange": 0,
  "attractionTags": {
    "property1": "string",
    "property2": "string"
  },
  "hotelTags": {
    "property1": "string",
    "property2": "string"
  },
  "status_tours": "string",
  "status_restos": "string",
  "status_hotels": "string"
}
```
:shipit::shipit::shipit:
