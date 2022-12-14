# coding: utf-8

"""
    Edge-API

    The Edge-API is built under the BIND5G project and its purpose is to act as an intermidiator between the NaaS API and the Kubernetes cluster. The NaaS API is a general API in respect of the project to remotely and automatically deploy, manage and control 5G and MEC infrastructures for a vast amount of experiments. On the other hand, the Edge-API is a specific backend API to manage Kubernetes resources and deploy application instances into the cluster.  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: mdalgitsis@vicomtech.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Service(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'service_name': 'str',
        'service_selector': 'object',
        'service_label': 'object',
        'service_port': 'list[list[object]]',
        'service_type': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'service_selector': 'service_selector',
        'service_label': 'service_label',
        'service_port': 'service_port',
        'service_type': 'service_type'
    }

    def __init__(self, service_name=None, service_selector=None, service_label=None, service_port=None, service_type=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501
        self._service_name = None
        self._service_selector = None
        self._service_label = None
        self._service_port = None
        self._service_type = None
        self.discriminator = None
        self.service_name = service_name
        self.service_selector = service_selector
        if service_label is not None:
            self.service_label = service_label
        self.service_port = service_port
        self.service_type = service_type

    @property
    def service_name(self):
        """Gets the service_name of this Service.  # noqa: E501


        :return: The service_name of this Service.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this Service.


        :param service_name: The service_name of this Service.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def service_selector(self):
        """Gets the service_selector of this Service.  # noqa: E501


        :return: The service_selector of this Service.  # noqa: E501
        :rtype: object
        """
        return self._service_selector

    @service_selector.setter
    def service_selector(self, service_selector):
        """Sets the service_selector of this Service.


        :param service_selector: The service_selector of this Service.  # noqa: E501
        :type: object
        """
        if service_selector is None:
            raise ValueError("Invalid value for `service_selector`, must not be `None`")  # noqa: E501

        self._service_selector = service_selector

    @property
    def service_label(self):
        """Gets the service_label of this Service.  # noqa: E501


        :return: The service_label of this Service.  # noqa: E501
        :rtype: object
        """
        return self._service_label

    @service_label.setter
    def service_label(self, service_label):
        """Sets the service_label of this Service.


        :param service_label: The service_label of this Service.  # noqa: E501
        :type: object
        """

        self._service_label = service_label

    @property
    def service_port(self):
        """Gets the service_port of this Service.  # noqa: E501


        :return: The service_port of this Service.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """Sets the service_port of this Service.


        :param service_port: The service_port of this Service.  # noqa: E501
        :type: list[list[object]]
        """
        if service_port is None:
            raise ValueError("Invalid value for `service_port`, must not be `None`")  # noqa: E501

        self._service_port = service_port

    @property
    def service_type(self):
        """Gets the service_type of this Service.  # noqa: E501

        Service types  # noqa: E501

        :return: The service_type of this Service.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this Service.

        Service types  # noqa: E501

        :param service_type: The service_type of this Service.  # noqa: E501
        :type: str
        """
        if service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ClusterIP", "LoadBalancer", "Ingress", "NodePort"]  # noqa: E501
        if service_type not in allowed_values:
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_type, allowed_values)
            )

        self._service_type = service_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Service, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
