# ec2\-no\-amazon\-key\-pair<a name="ec2-no-amazon-key-pair"></a>

Checks if running Amazon Elastic Compute Cloud \(EC2\) instances are launched using amazon key pairs\. The rule is NON\_COMPLIANT if a running EC2 instance is launched with a key pair\. 

**Identifier:** EC2\_NO\_AMAZON\_KEY\_PAIR

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d221c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.