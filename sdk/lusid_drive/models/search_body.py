# coding: utf-8

"""
    FINBOURNE Drive API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.229
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class SearchBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'with_path': 'str',
        'name': 'str'
    }

    attribute_map = {
        'with_path': 'withPath',
        'name': 'name'
    }

    required_map = {
        'with_path': 'optional',
        'name': 'required'
    }

    def __init__(self, with_path=None, name=None):  # noqa: E501
        """
        SearchBody - a model defined in OpenAPI

        :param with_path:  Optional path field to limit the search to result with a matching (case insensitive) path
        :type with_path: str
        :param name:  Name of the file or folder to be searched (required)
        :type name: str

        """  # noqa: E501

        self._with_path = None
        self._name = None
        self.discriminator = None

        self.with_path = with_path
        self.name = name

    @property
    def with_path(self):
        """Gets the with_path of this SearchBody.  # noqa: E501

        Optional path field to limit the search to result with a matching (case insensitive) path  # noqa: E501

        :return: The with_path of this SearchBody.  # noqa: E501
        :rtype: str
        """
        return self._with_path

    @with_path.setter
    def with_path(self, with_path):
        """Sets the with_path of this SearchBody.

        Optional path field to limit the search to result with a matching (case insensitive) path  # noqa: E501

        :param with_path: The with_path of this SearchBody.  # noqa: E501
        :type: str
        """
        if with_path is not None and len(with_path) > 512:
            raise ValueError("Invalid value for `with_path`, length must be less than or equal to `512`")  # noqa: E501
        if with_path is not None and len(with_path) < 1:
            raise ValueError("Invalid value for `with_path`, length must be greater than or equal to `1`")  # noqa: E501
        if (with_path is not None and not re.search(r'^[\/a-zA-Z0-9 \-_]+$', with_path)):  # noqa: E501
            raise ValueError(r"Invalid value for `with_path`, must be a follow pattern or equal to `/^[\/a-zA-Z0-9 \-_]+$/`")  # noqa: E501

        self._with_path = with_path

    @property
    def name(self):
        """Gets the name of this SearchBody.  # noqa: E501

        Name of the file or folder to be searched  # noqa: E501

        :return: The name of this SearchBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchBody.

        Name of the file or folder to be searched  # noqa: E501

        :param name: The name of this SearchBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (name is not None and not re.search(r'^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$/`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
