# Breanna Bisnott ECSE3038 Lab 2 Submission
*My favourite Pokemon is Eevee, simply because she was cute when I googled, 'Pokemon Names'*

The purpose of this code is for a lab assignment on building POST request handlers with FastAPI :D

## `post_person()`

The `post_person()` function will update a list every time a post request is handled. The post request handler accepts incoming requests at the `/person` route. The post request handler check's if the request body's three keys have an associated value.

If the three keys have an associated value, the list will be posted and if not, an error message will be posted. See sample requests & responses below:

### *sample request*

POST /person  

{  
	"name": "Beef Wellington",  
	"occupation": "Fry Cook",  
	"address": "124 Conch Street"  
}

### *sample response*
{  
	"success": true,  
	"result": {  
		"name": "Beef Wellington",  
		"occupation": "Fry Cook",  
		"address": "124 Conch Street"  
  }  
}  

### *sample request*
POST /person

{  
	"name": "Beef Wellington",  
	"occupation": "Fry Cook",  
	"address": ""  
}  


### *sample response*

{  
	"success": false,  
	"result": {  
		"error_message": "invalid request"  
  }  
}  

## `get_person()`

The `get_person()` function will retrieve a list of all existing people's information in the data list. The GET request handler accepts incoming requests at the `/person` route.

### *sample request*
GET /person

### *sample response*
{  
  "name": "Beef Wellington",  
  "occupation": "Fry Cook",  
  "address": "124 Conch Street"  
},  
{  
  "name": "Star Stone",  
  "occupation": "Scientist",  
  "address": "122 Conch Street"  
}
