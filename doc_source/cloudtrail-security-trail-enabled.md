# cloudtrail\-security\-trail\-enabled<a name="cloudtrail-security-trail-enabled"></a>

Checks that there is at least one AWS CloudTrail trail defined with security best practices\. This rule is COMPLIANT if there is at least one trail that meets all of the following:
+ records global service events
+ is a multi\-region trail
+ has Log file validation enabled
+ encrypted with a KMS key
+ records events for reads and writes
+ records management events
+ does not exclude any management events

This rule is NON\_COMPLIANT if no trails meet all of the criteria mentioned above\.

**Identifier:** CLOUDTRAIL\_SECURITY\_TRAIL\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17c61c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.