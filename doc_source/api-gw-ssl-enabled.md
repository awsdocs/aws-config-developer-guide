# api\-gw\-ssl\-enabled<a name="api-gw-ssl-enabled"></a>

Checks if a REST API stage uses an Secure Sockets Layer \(SSL\) certificate\. This rule is NON\_COMPLIANT if the REST API stage does not have an associated SSL certificate\. 

**Identifier:** API\_GW\_SSL\_ENABLED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

CertificateIDs \(Optional\)Type: CSV  
Comma\-separated list of client certificate IDs configured on a REST API stage\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c29c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.