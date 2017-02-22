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

class PolicyTagAssociationDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'networkDevices': 'list[PolicyTagAssociationDeviceDTO]',
            
            
            'policyTag': 'str',
            
            
            'unModifiableReason': 'str',
            
            
            'unModifiable': 'bool'
            
        }

        self.attributeMap = {
            
            'networkDevices': 'networkDevices',
            
            'policyTag': 'policyTag',
            
            'unModifiableReason': 'unModifiableReason',
            
            'unModifiable': 'unModifiable'
            
        }       

        
        
        self.networkDevices = None # list[PolicyTagAssociationDeviceDTO]
        
        
        self.policyTag = None # str
        
        
        self.unModifiableReason = None # str
        
        
        self.unModifiable = None # bool
        
