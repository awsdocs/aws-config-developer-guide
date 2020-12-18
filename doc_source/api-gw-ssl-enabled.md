# api\-gw\-ssl\-enabled<a name="api-gw-ssl-enabled"></a>

Checks if a REST API stage uses a Secure Sockets Layer \(SSL\) certificate\. This rule is COMPLIANT if the REST API stage has an associated SSL certificate\. This rule is NON\_COMPLIANT if the REST API stage does not have an associated SSL certificate, or if a certificate ID is provided as a parameter and does not match the `CertificateIDs` parameter list\. 

**Identifier:** API\_GW\_SSL\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), and AWS GovCloud \(US\-West\)

**Parameters:**

CertificateIDs \(Optional\)Type: CSV  
Comma\-separated list of client certificate IDs configured on a REST API stage\.

## AWS CloudFormation template<a name="w24aac11c29c17c27c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.