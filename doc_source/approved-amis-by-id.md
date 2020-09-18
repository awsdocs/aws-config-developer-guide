# approved\-amis\-by\-id<a name="approved-amis-by-id"></a>

Checks whether running instances are using specified AMIs\. Specify a list of approved AMI IDs\. Running instances with AMIs that are not on this list are NON\_COMPLIANT\.

**Identifier:** APPROVED\_AMIS\_BY\_ID

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 amiIds   
The AMI IDs \(comma\-separated list of up to 10\)\.

## AWS CloudFormation template<a name="w22aac11c29c17c31c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.