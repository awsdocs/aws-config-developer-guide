# access\-keys\-rotated<a name="access-keys-rotated"></a>

Checks if the active access keys are rotated within the number of days specified in `maxAccessKeyAge`\. The rule is NON\_COMPLIANT if the access keys have not been rotated for more than `maxAccessKeyAge` number of days\.

**Note**  
This rule requires you to turn on 'Include global resources' in general settings in order for resources to be evaluated\.  
Re\-evaluating this rule within 4 hours of the first evaluation will have no effect on the results\.

**Identifier:** ACCESS\_KEYS\_ROTATED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

maxAccessKeyAgeType: intDefault: 90  
Maximum number of days without rotation\. Default 90\.

## AWS CloudFormation template<a name="w79aac11c32c17b9b1c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.