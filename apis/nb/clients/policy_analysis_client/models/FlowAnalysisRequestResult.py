#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowAnalysisRequestResult(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'flowAnalysisId': 'str',
            
            
            'url': 'str',
            
            
            'taskId': 'str'
            
        }

        self.attributeMap = {
            
            'flowAnalysisId': 'flowAnalysisId',
            
            'url': 'url',
            
            'taskId': 'taskId'
            
        }       

        
        
        self.flowAnalysisId = None # str
        
        
        self.url = None # str
        
        
        self.taskId = None # str
        
