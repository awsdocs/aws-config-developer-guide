# encrypted\-volumes<a name="encrypted-volumes"></a>

Checks whether the EBS volumes that are in an attached state are encrypted\. If you specify the ID of a KMS key for encryption using the kmsId parameter, the rule checks if the EBS volumes in an attached state are encrypted with that KMS key\.

For more information, see [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the *Amazon EC2 User Guide for Linux Instances*\.

**Identifier:** ENCRYPTED\_VOLUMES

**Trigger type:** Configuration changes

**Parameters:**

 kmsId   
 ID or ARN of the KMS key that is used to encrypt the volume\. 

## AWS CloudFormation template<a name="w4aac13c29c17d153c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.