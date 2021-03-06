# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.import logging
from django.utils.translation import ugettext as _

class Argument():
  _type = None
  def __init__(self, name, description=None):
    self._name = name
    self._description = _(description if description else name)

  @property
  def name(self):
    return self._name

  @property
  def type(self):
    return self._type

  def to_dict(self):
    return {"name": self._name, "type": self._type, "description": self._description}

class TextArgument(Argument):
  _type = "text"

class CheckboxArgument(Argument):
  _type = "checkbox"

class MappingArgument(Argument):
  _type = "mapping"