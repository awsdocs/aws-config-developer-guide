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

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d109c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.