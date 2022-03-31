# approved\-amis\-by\-tag<a name="approved-amis-by-tag"></a>

Checks if running instances are using specified AMIs\. Specify the tags that identify the AMIs\. Running instances with AMIs that don't have at least one of the specified tags are NON\_COMPLIANT\.

**Identifier:** APPROVED\_AMIS\_BY\_TAG

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

amisByTagKeyAndValueType: StringMapDefault: tag\-key:tag\-value,other\-tag\-key  
The AMIs by tag \(comma\-separated list up to 10; for example,`tag-key:tag-value`; i\.e\. `tag-key1` matches AMIs with `tag-key1`,`tag-key2:value2` matches `tag-key2` having value2\)\.

## AWS CloudFormation template<a name="w76aac11c31c17b7c27c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.