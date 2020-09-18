# root\-account\-hardware\-mfa\-enabled<a name="root-account-hardware-mfa-enabled"></a>

Checks whether your AWS account is enabled to use multi\-factor authentication \(MFA\) hardware device to sign in with root credentials\. The rule is NON\_COMPLIANT if any virtual MFA devices are permitted for signing in with root credentials\.

**Identifier:** ROOT\_ACCOUNT\_HARDWARE\_MFA\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), and AWS GovCloud \(US\-West\)

**Parameters:**

 None   

## AWS CloudFormation template<a name="w22aac11c29c17d275c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.