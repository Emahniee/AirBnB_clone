#!/usr/bin/python3
"""BaseModel for Airbnb Project"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """Base class for classes"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, time_format)
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
         """Returns string representation of an instance"""
         class_name = self.__class__.__name__
         return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
    
    def save(self):
         """updates the current datetime after changes"""
         self.updated_at = datetime.now()
         models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values"""
        ndict = self.__dict__.copy()
        ndict.update({"created_at": self.created_at.isoformat()})
        ndict.update({"updated_at": self.updated_at.isoformat()})
        ndict.update({"__class__": self.__class__.__name__})
        return (ndict)
