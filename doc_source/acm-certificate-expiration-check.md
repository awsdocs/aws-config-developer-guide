# acm\-certificate\-expiration\-check<a name="acm-certificate-expiration-check"></a>

Checks if AWS Certificate Manager Certificates in your account are marked for expiration within the specified number of days\. Certificates provided by ACM are automatically renewed\. ACM does not automatically renew certificates that you import\. The rule is NON\_COMPLIANT if your certificates are about to expire\.

**Identifier:** ACM\_CERTIFICATE\_EXPIRATION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), Asia Pacific \(Osaka\), Europe \(Milan\) Region

**Parameters:**

daysToExpiration \(Optional\)Type: intDefault: 14  
Specify the number of days before the rule flags the ACM Certificate as noncompliant\.

## AWS CloudFormation template<a name="w29aac11c33c17b7b5c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.