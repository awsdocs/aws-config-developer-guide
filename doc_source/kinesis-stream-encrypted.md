# kinesis\-stream\-encrypted<a name="kinesis-stream-encrypted"></a>

Checks if Amazon Kinesis streams are encrypted at rest with server\-side encryption\. The rule is NON\_COMPLIANT for a Kinesis stream if 'StreamEncryption' is not present\. 

**Identifier:** KINESIS\_STREAM\_ENCRYPTED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w79aac11c32c17b9d357c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.