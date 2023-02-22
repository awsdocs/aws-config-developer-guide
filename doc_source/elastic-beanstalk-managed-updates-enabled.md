# elastic\-beanstalk\-managed\-updates\-enabled<a name="elastic-beanstalk-managed-updates-enabled"></a>

Checks if managed platform updates in an AWS Elastic Beanstalk environment is enabled\. The rule is COMPLIANT if the value for `ManagedActionsEnabled` is set to true\. The rule is NON\_COMPLIANT if the value for `ManagedActionsEnabled` is set to false, or if a parameter is provided and its value does not match the existing configurations\. 

**Identifier:** ELASTIC\_BEANSTALK\_MANAGED\_UPDATES\_ENABLED

**Resource Types:** AWS::ElasticBeanstalk::Environment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

UpdateLevel \(Optional\)Type: String  
Indicates whether update levels are set to 'minor' version updates or a 'patch' version updates\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d291c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.