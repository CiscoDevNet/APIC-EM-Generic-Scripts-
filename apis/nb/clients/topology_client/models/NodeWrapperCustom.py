#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2015 Reverb Technologies, Inc.

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

class NodeWrapperCustom(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'label': 'str',
            
            
            'parentNodeId': 'str',
            
            
            'y': 'int',
            
            
            'x': 'int',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'label': 'label',
            
            'parentNodeId': 'parentNodeId',
            
            'y': 'y',
            
            'x': 'x',
            
            'id': 'id'
            
        }       

        
        #Label for the node
        
        self.label = None # str
        
        #Unique Id of the Node for ehich the custom properties are being represented
        
        self.parentNodeId = None # str
        
        #Y - Coordinate for this Node in the topology View
        
        self.y = None # int
        
        #X - Coordinate for this Node in the topology View
        
        self.x = None # int
        
        
        self.id = None # str
        
