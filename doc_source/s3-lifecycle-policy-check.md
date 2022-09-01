# s3\-lifecycle\-policy\-check<a name="s3-lifecycle-policy-check"></a>

Checks if a lifecycle rule is configured for an Amazon Simple Storage Service \(Amazon S3\) bucket\. The rule is NON\_COMPLIANT if there is no active lifecycle configuration rules or the configuration does not match with the parameter values\. 

**Identifier:** S3\_LIFECYCLE\_POLICY\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

targetTransitionDays \(Optional\)Type: int  
Number of days after object creation when objects are transitioned to a specified storage class \(for example, 30 days\)\.

targetExpirationDays \(Optional\)Type: int  
Number of days after object creation when objects are deleted \(for example, 395 days\)\.

targetTransitionStorageClass \(Optional\)Type: String  
Destination storage class type \(for example, Amazon S3 Standard\-Infrequent Access \(S3 Standard\-IA\)\. For more information, see https: //docs\.aws\.amazon\.com/AmazonS3/latest/dev/storage\-class\-intro\.html\.

targetPrefix \(Optional\)Type: String  
Amazon S3 Object prefix to identify one or more objects\.

bucketNames \(Optional\)Type: CSV  
Comma\-separated list of Amazon S3 bucket names that have lifecycle policy enabled\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d509c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.