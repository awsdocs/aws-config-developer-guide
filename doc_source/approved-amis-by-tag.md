# approved\-amis\-by\-tag<a name="approved-amis-by-tag"></a>

Checks whether running instances are using specified AMIs\. Specify the tags that identify the AMIs\. Running instances with AMIs that don't have at least one of the specified tags are NON\_COMPLIANT\.

**Identifier:** APPROVED\_AMIS\_BY\_TAG

**Trigger type:** Configuration changes

**Parameters:**

 amisByTagKeyAndValue   
The AMIs by tag \(comma\-separated list up to 10; for example, "tag\-key:tag\-value"\)\.

## AWS CloudFormation template<a name="w4aac13c29c17c47c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.