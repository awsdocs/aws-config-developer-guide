# elastic\-beanstalk\-managed\-updates\-enabled<a name="elastic-beanstalk-managed-updates-enabled"></a>

Rule will evaluate if managed platform updates in Elastic Beanstalk environments are ENABLED\. This rule is NON\_COMPLIANT if the value for 'ManagedActionsEnabled' is set to 'false' 

**Identifier:** ELASTIC\_BEANSTALK\_MANAGED\_UPDATES\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

UpdateLevel \(Optional\)Type: String  
UpdateLevel: \(optional\): A parameter for platform update, to check if updates level will be a 'minor' version update, or a 'patch'

## AWS CloudFormation template<a name="w24aac11c29c17b7d159c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.