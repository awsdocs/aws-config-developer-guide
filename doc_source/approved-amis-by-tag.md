# approved\-amis\-by\-tag<a name="approved-amis-by-tag"></a>

Checks whether running instances are using specified AMIs\. 

**Identifier:** APPROVED\_AMIS\_BY\_TAG

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

amisByTagKeyAndValueType: StringMapDefault: tag\-key:tag\-value,other\-tag\-key  
Specify AMIs by tag \(comma separated list up to 10; for example, 'tag\-key:tag\-value'\)\.

## AWS CloudFormation template<a name="w24aac11c29c17b7c25c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.