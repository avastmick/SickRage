# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions.
    The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class SeriesActorsData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, image=None, image_added=None, image_author=None, last_updated=None, name=None, role=None, series_id=None, sort_order=None):
        """
        SeriesActorsData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'image': 'str',
            'image_added': 'str',
            'image_author': 'int',
            'last_updated': 'str',
            'name': 'str',
            'role': 'str',
            'series_id': 'int',
            'sort_order': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'image': 'image',
            'image_added': 'imageAdded',
            'image_author': 'imageAuthor',
            'last_updated': 'lastUpdated',
            'name': 'name',
            'role': 'role',
            'series_id': 'seriesId',
            'sort_order': 'sortOrder'
        }

        self._id = id
        self._image = image
        self._image_added = image_added
        self._image_author = image_author
        self._last_updated = last_updated
        self._name = name
        self._role = role
        self._series_id = series_id
        self._sort_order = sort_order

    @property
    def id(self):
        """
        Gets the id of this SeriesActorsData.


        :return: The id of this SeriesActorsData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SeriesActorsData.


        :param id: The id of this SeriesActorsData.
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """
        Gets the image of this SeriesActorsData.


        :return: The image of this SeriesActorsData.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this SeriesActorsData.


        :param image: The image of this SeriesActorsData.
        :type: str
        """

        self._image = image

    @property
    def image_added(self):
        """
        Gets the image_added of this SeriesActorsData.


        :return: The image_added of this SeriesActorsData.
        :rtype: str
        """
        return self._image_added

    @image_added.setter
    def image_added(self, image_added):
        """
        Sets the image_added of this SeriesActorsData.


        :param image_added: The image_added of this SeriesActorsData.
        :type: str
        """

        self._image_added = image_added

    @property
    def image_author(self):
        """
        Gets the image_author of this SeriesActorsData.


        :return: The image_author of this SeriesActorsData.
        :rtype: int
        """
        return self._image_author

    @image_author.setter
    def image_author(self, image_author):
        """
        Sets the image_author of this SeriesActorsData.


        :param image_author: The image_author of this SeriesActorsData.
        :type: int
        """

        self._image_author = image_author

    @property
    def last_updated(self):
        """
        Gets the last_updated of this SeriesActorsData.


        :return: The last_updated of this SeriesActorsData.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this SeriesActorsData.


        :param last_updated: The last_updated of this SeriesActorsData.
        :type: str
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """
        Gets the name of this SeriesActorsData.


        :return: The name of this SeriesActorsData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SeriesActorsData.


        :param name: The name of this SeriesActorsData.
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """
        Gets the role of this SeriesActorsData.


        :return: The role of this SeriesActorsData.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this SeriesActorsData.


        :param role: The role of this SeriesActorsData.
        :type: str
        """

        self._role = role

    @property
    def series_id(self):
        """
        Gets the series_id of this SeriesActorsData.


        :return: The series_id of this SeriesActorsData.
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """
        Sets the series_id of this SeriesActorsData.


        :param series_id: The series_id of this SeriesActorsData.
        :type: int
        """

        self._series_id = series_id

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SeriesActorsData.


        :return: The sort_order of this SeriesActorsData.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SeriesActorsData.


        :param sort_order: The sort_order of this SeriesActorsData.
        :type: int
        """

        self._sort_order = sort_order

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
