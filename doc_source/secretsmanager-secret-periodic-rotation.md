# secretsmanager\-secret\-periodic\-rotation<a name="secretsmanager-secret-periodic-rotation"></a>

Checks if AWS Secrets Manager secrets have been rotated in the past specified number of days\. The rule is NON\_COMPLIANT if a secret has not been rotated for more than maxDaysSinceRotation number of days\. The default value is 90 days\.

**Identifier:** SECRETSMANAGER\_SECRET\_PERIODIC\_ROTATION

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

maxDaysSinceRotation \(Optional\)Type: int  
Maximum number of days in which a secret can remain unchanged\. The default value is 90 days\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d569c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.