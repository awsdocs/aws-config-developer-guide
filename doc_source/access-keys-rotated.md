# access\-keys\-rotated<a name="access-keys-rotated"></a>

Checks whether the active access keys are rotated within the number of days specified in `maxAccessKeyAge`\. The rule is NON\_COMPLIANT if the access keys have not been rotated for more than `maxAccessKeyAge` number of days\.

**Note**  
Re\-evaluating this rule within 4 hours of the first evaluation will have no effect on the results\. 

**Identifier:** ACCESS\_KEYS\_ROTATED

**Trigger type:** Periodic

**Parameters:**

 maxAccessKeyAge  
Maximum number of days within which the access keys must be rotated\. The default value is 90 days\.

## AWS CloudFormation template<a name="w4aac13c29c17c33c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.