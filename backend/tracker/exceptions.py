from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _

class NoContentException(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = _('No content found.')
    default_code = 'no_content'