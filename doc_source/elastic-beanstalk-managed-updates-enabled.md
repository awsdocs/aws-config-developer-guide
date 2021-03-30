# elastic\-beanstalk\-managed\-updates\-enabled<a name="elastic-beanstalk-managed-updates-enabled"></a>

Checks if managed platform updates in an AWS Elastic Beanstalk environment is enabled\. The rule is COMPLIANT if the value for `ManagedActionsEnabled` is set to true\. The rule is NON\_COMPLIANT if the value for `ManagedActionsEnabled` is set to false, or if a parameter is provided and its value does not match the existing configurations\. 

**Identifier:** ELASTIC\_BEANSTALK\_MANAGED\_UPDATES\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

UpdateLevel \(Optional\)Type: String  
UpdateLevel: \(optional\): A parameter for platform update, to check if updates level will be a 'minor' version update, or a 'patch'

## AWS CloudFormation template<a name="w26aac11c31c17b7d159c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.