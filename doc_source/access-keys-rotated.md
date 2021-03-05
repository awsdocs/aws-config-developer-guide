# access\-keys\-rotated<a name="access-keys-rotated"></a>

Checks whether the active access keys are rotated within the number of days specified in `maxAccessKeyAge`\. The rule is non\-compliant if the access keys have not been rotated for more than `maxAccessKeyAge` number of days\. 

**Identifier:** ACCESS\_KEYS\_ROTATED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

maxAccessKeyAgeType: intDefault: 90  
Maximum number of days without rotation\. Default 90\.

## AWS CloudFormation template<a name="w24aac11c29c17b7b1c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.