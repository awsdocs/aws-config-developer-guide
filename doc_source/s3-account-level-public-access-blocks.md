# s3\-account\-level\-public\-access\-blocks<a name="s3-account-level-public-access-blocks"></a>

Checks whether the required public access block settings are configured from account level\. The rule is NON\_COMPLIANT when the public access block settings are not configured from account level\. 

**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Europe \(Milan\), Middle East \(Bahrain\) Region

**Parameters:**

IgnorePublicAcls \(Optional\)Type: StringDefault: True  
IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy \(Optional\)Type: StringDefault: True  
BlockPublicPolicy is enforced or not, default True

BlockPublicAcls \(Optional\)Type: StringDefault: True  
BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets \(Optional\)Type: StringDefault: True  
RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template<a name="w24aac11c29c17b7d291c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.