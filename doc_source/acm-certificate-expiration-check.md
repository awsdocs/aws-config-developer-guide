# acm\-certificate\-expiration\-check<a name="acm-certificate-expiration-check"></a>

Checks whether ACM Certificates in your account are marked for expiration within the specified number of days\. Certificates provided by ACM are automatically renewed\. ACM does not automatically renew certificates that you import\.

**Identifier:** ACM\_CERTIFICATE\_EXPIRATION\_CHECK

**Trigger type:** Configuration changes and periodic

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 daysToExpiration   
Specify the number of days before the rule flags the ACM Certificate as NON\_COMPLIANT\.

## AWS CloudFormation template<a name="w22aac11c29c17c17c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.