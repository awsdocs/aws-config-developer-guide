# acm\-certificate\-rsa\-check<a name="acm-certificate-rsa-check"></a>

Checks if RSA certificates managed by AWS Certificate Manager \(ACM\) have a key length of at least '2048' bits\.The rule is NON\_COMPLIANT if the minimum key length is less than 2048 bits\. 

**Identifier:** ACM\_CERTIFICATE\_RSA\_CHECK

**Resource Types:** AWS::ACM::Certificate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9b7c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.