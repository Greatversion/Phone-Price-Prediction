**Phone Price Prediction API**
==========================

**Overview**
------------

This API uses machine learning models to predict the price of a phone based on its features. The API has two endpoints, one for a linear regression model and one for a random forest model.

**Endpoints**
------------

### Linear Regression Model

* **URL:** https://phone-price-prediction-2z4u.onrender.com/linear
* **Method:** POST
* **Request Body:** JSON object with the following features:
	+ `features`: an array of 7 numbers representing the phone's features:
		- Screen size (in inches)
		- RAM (in GB)
		- Storage (in GB)
		- Battery life (in hours)
		- Rear camera resolution (in megapixels)
		- Front camera resolution (in megapixels)
		- Battery capacity (in mAh)

**Example Request:**
```json
{
  "features": [
    4.3, 
    4.0, 
    128.0, 
    6.0, 
    48,
    13.0,
    4000
  ]
}
```

**Example Response:**
```json
{
  "predicted_price": 599.99
}
```

### Random Forest Model

* **URL:** https://phone-price-prediction-2z4u.onrender.com/random
* **Method:** POST
* **Request Body:** Same as the linear regression model

**Example Request:**
```json
{
  "features": [
    4.3, 
    4.0, 
    128.0, 
    6.0, 
    48,
    13.0,
    4000
  ]
}
```

**Example Response:**
```json
{
  "predicted_price": 649.99
}
```

**Usage**
-----

1. Send a POST request to the desired endpoint with the phone's features in the request body.
2. The API will respond with a JSON object containing the predicted price.

