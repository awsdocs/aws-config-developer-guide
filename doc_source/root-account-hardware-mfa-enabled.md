# root\-account\-hardware\-mfa\-enabled<a name="root-account-hardware-mfa-enabled"></a>

Checks if your AWS account is enabled to use multi\-factor authentication \(MFA\) hardware device to sign in with root credentials\. The rule is NON\_COMPLIANT if any virtual MFA devices are permitted for signing in with root credentials\.

**Identifier:** ROOT\_ACCOUNT\_HARDWARE\_MFA\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d509c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.