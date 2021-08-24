# encrypted\-volumes<a name="encrypted-volumes"></a>

Checks if the EBS volumes that are in an attached state are encrypted\. If you specify the ID of a KMS key for encryption using the kmsId parameter, the rule checks if the EBS volumes in an attached state are encrypted with that KMS key\.

**Identifier:** ENCRYPTED\_VOLUMES

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

kmsId \(Optional\)Type: String  
ID or ARN of the KMS key that is used to encrypt the volume\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d211c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.