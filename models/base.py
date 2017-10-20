import abc
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base():

    @abc.abstractmethod
    def _to_jsonize(self):
        """Returns the field names to serialize for this model."""
        return []

    @property
    def serialize(self):
        result = {}
        for key in self._to_jsonize():
            result[key] = getattr(self, key)
        return result
