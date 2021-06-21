# ImageAPI
An API where you can share labeled images and generate color pallets for images.

# Usage
Run `uvicorn main:app` in the terminal.

Go to `https://<your url>/docs` to view the documentation.

# How it works
* When you make a post request to the api it converts the image to a png format and stores it in the images directory.
* A database entery is created to store the path to the image along with the label that goes with it.
* When you make a get requests the stored image is returned.