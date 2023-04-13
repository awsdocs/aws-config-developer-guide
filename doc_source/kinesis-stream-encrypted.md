# kinesis\-stream\-encrypted<a name="kinesis-stream-encrypted"></a>

Checks if Amazon Kinesis streams are encrypted at rest with server\-side encryption\. The rule is NON\_COMPLIANT for a Kinesis stream if 'StreamEncryption' is not present\. 

**Identifier:** KINESIS\_STREAM\_ENCRYPTED

**Resource Types:** AWS::Kinesis::Stream

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d393c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.