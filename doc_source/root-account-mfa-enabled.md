# root\-account\-mfa\-enabled<a name="root-account-mfa-enabled"></a>

Checks if your AWS account is enabled to use multi\-factor authentication \(MFA\) hardware device to sign in with root credentials\. The rule is NON\_COMPLIANT if any virtual MFA devices are permitted for signing in with root credentials\.

**Identifier:** ROOT\_ACCOUNT\_MFA\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d301c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.