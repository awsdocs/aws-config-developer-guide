# secretsmanager\-secret\-unused<a name="secretsmanager-secret-unused"></a>

Checks if AWS Secrets Manager secrets have been accessed within a specified number of days\. The rule is NON\_COMPLIANT if a secret has not been accessed in ‘unusedForDays’ number of days\. The default value is 90 days\.

**Identifier:** SECRETSMANAGER\_SECRET\_UNUSED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

unusedForDays \(Optional\)Type: int  
The number of days in which a secret can remain unused\. The default value is 90 days\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d527c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.