# approved\-amis\-by\-id<a name="approved-amis-by-id"></a>

Checks if running instances are using specified AMIs\. Specify a list of approved AMI IDs\. Running instances with AMIs that are not on this list are NON\_COMPLIANT\.

**Identifier:** APPROVED\_AMIS\_BY\_ID

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

amiIdsType: CSV  
The AMI IDs \(comma\-separated list of up to 21 AMI IDs or 1024 characters total, whichever comes first\)\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c31c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.