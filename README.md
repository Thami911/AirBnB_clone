0x00. AirBnB clone- The console Project by Thulani Ndlovu and Thami Mncwabe

Task List

0. README, Authors
- Write a readme file with the discription of the project
- Write the desciption of the command interpreter; How to start it, how to use it, examples.
- Write an AUTHORS file listing all the individuals having contributed to the repository




1. Be pycodestyle compliant!
- Write beautiful code that passes the pycodestyle check




2. Unittests
- All the files, classes, functions must be tested with unittests




3. BaseModel
- Write a class BaseModel that defines all common attributes/methods for other classes:
- models/base_model.py




4. Create BaseModel from dictionary
- Create an instance with the dictionary representation to_dict().




5. Store first object
- Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
- Update "models/__init__.py" to create a unique FileStorage instance for your application.
- Update "models/base_models.py" to link your BaseModel to FileStorage by using the variable "storage"




6. Console 0.0.1
- Write a program called "console.py" that contains the entry point of the command interpreter.




7. Console 0.1
- Update command interpreter "console.py" to have the following commands:
- create
- show
- destroy
- all
- update




8. First User
- Write a class User that inherits from BaseModel.
- Update Filestorage to manage correctly serialization and deserialization of User.
- Update command interpreter (console.py) to allow show, create, destroy, update, and all used with User.




9. More classes
- Write all those classes that inherit from BaseModel:
- State (models/state.py)
- City (models/city.py)
- Amenity (models/amenity.py
- Place (models/place.py)
- Review (models/review.py)




10. Console 1.0
- Update Filestorage to manage correctly serialization and deserialization of all our new classes:
- Place
- State
- City
- Amenity
- Review

- Update command interpreter (console.py) to allow the actions below:
- show
- create
- destroy
- update
- all
