# s3\-account\-level\-public\-access\-blocks\-periodic<a name="s3-account-level-public-access-blocks-periodic"></a>

Checks if the required public access block settings are configured from account level\. 

**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS\_PERIODIC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

IgnorePublicAcls \(Optional\)Type: String  
IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy \(Optional\)Type: String  
BlockPublicPolicy is enforced or not, default True

BlockPublicAcls \(Optional\)Type: String  
BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets \(Optional\)Type: String  
RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template<a name="w2aac12c33c15b9d515c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.