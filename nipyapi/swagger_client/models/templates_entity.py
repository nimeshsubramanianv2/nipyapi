# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TemplatesEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'templates': 'list[TemplateEntity]',
        'generated': 'str'
    }

    attribute_map = {
        'templates': 'templates',
        'generated': 'generated'
    }

    def __init__(self, templates=None, generated=None):
        """
        TemplatesEntity - a model defined in Swagger
        """

        self._templates = None
        self._generated = None

        if templates is not None:
          self.templates = templates
        if generated is not None:
          self.generated = generated

    @property
    def templates(self):
        """
        Gets the templates of this TemplatesEntity.

        :return: The templates of this TemplatesEntity.
        :rtype: list[TemplateEntity]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this TemplatesEntity.

        :param templates: The templates of this TemplatesEntity.
        :type: list[TemplateEntity]
        """

        self._templates = templates

    @property
    def generated(self):
        """
        Gets the generated of this TemplatesEntity.
        When this content was generated.

        :return: The generated of this TemplatesEntity.
        :rtype: str
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """
        Sets the generated of this TemplatesEntity.
        When this content was generated.

        :param generated: The generated of this TemplatesEntity.
        :type: str
        """

        self._generated = generated

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TemplatesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
