# encrypted\-volumes<a name="encrypted-volumes"></a>

Checks whether EBS volumes that are in an attached state are encrypted\. 

**Identifier:** ENCRYPTED\_VOLUMES

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

kmsId \(Optional\)Type: String  
ID or ARN of the KMS key that is used to encrypt the volume\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d179c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.