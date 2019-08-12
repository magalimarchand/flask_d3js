########################################################
************   MIND-IN-A-BOX CONVERTERS   *************
########################################################


The mib_interface converters folder contains methods and classes to convert and format all types of data imported into the application from different sources: 
Splunk, Elasticsearch, Centreon, databases, CSV, JSON, etc.

It helps standardize the data in order to use it in the various custom visualizations 
available in the application.


In order for the custom visualizations to be re-usable and exportable to any programming language and framework, the MIB converters transform all data to JSON format.