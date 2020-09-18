# lambda\-function\-settings\-check<a name="lambda-function-settings-check"></a>

Checks that the lambda function settings for runtime, role, timeout, and memory size match the expected values\.

**Identifier:** LAMBDA\_FUNCTION\_SETTINGS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Ningxia\)

**Parameters:**

 runtime  
Comma\-separated list of runtime values\. 

 role  
IAM role\.

 timeout  
Timeout in seconds\.

 memorySize  
Memory size in MB\.

## AWS CloudFormation template<a name="w22aac11c29c17d229c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.