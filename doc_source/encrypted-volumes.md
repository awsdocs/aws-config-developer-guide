# encrypted\-volumes<a name="encrypted-volumes"></a>

Checks if the EBS volumes that are in an attached state are encrypted\. If you specify the ID of a KMS key for encryption using the kmsId parameter, the rule checks if the EBS volumes in an attached state are encrypted with that KMS key\.

**Identifier:** ENCRYPTED\_VOLUMES

**Resource Types:** AWS::EC2::Volume

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsId \(Optional\)Type: String  
ID or ARN of the KMS key that is used to encrypt the volume\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d315c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.