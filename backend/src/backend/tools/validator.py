""" Exceptions classes based on http exceptions """

from abc import ABC, abstractmethod
import json
from typing import List
from fastapi import HTTPException, status


class Validator(ABC):
    """ Raise when any format error is reached. """

    def __init__(self):
        self._messages_codes: List[dict[str, str]] = []

    def validate_and_throw(self, request):
        """ Execute validations """
        self.__validate__(request)
        if len(self._messages_codes) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=json.dumps(self._messages_codes)
            )

    def any_error(self) -> bool:
        """ return true when any error was collected """
        return len(self._messages_codes) > 0

    def add_failure(self, code_message: tuple[str, str]):
        """ Add a message code into collection. """
        code, message = code_message
        self._messages_codes.append({'code': code, 'message': message})

    def as_error(self, code_message: tuple[str, str]):
        """ Raise a single Validation Error """
        code, message = code_message
        self._messages_codes.append({'code': code, 'message': message})
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=self._messages_codes
        )

    def as_not_found(self, code_message: tuple[str, str]):
        """ Raise a single Not Found Error """
        code, message = code_message
        self._messages_codes.append({'code': code, 'message': message})
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=self._messages_codes
        )

    def as_duplicated(self, code_message: tuple[str, str]):
        """ Raise a single  Duplicated Error """
        code, message = code_message
        self._messages_codes.append({'code': code, 'message': message})
        return HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=self._messages_codes
        )

    @abstractmethod
    def __validate__(self, request):
        """ Validate request format

            Abstract method.
        """
