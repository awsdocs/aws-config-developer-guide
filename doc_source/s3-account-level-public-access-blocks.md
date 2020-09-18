# s3\-account\-level\-public\-access\-blocks<a name="s3-account-level-public-access-blocks"></a>

Checks whether the required public access block settings are configured from account level\. The rule is only NON\_COMPLIANT when the fields set below do not match the corresponding fields in the configuration item\.

**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Middle East \(Bahrain\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

ignorePublicAcls  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\. 

blockPublicPolicy  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

blockPublicAcls  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

restrictPublicBuckets  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

## AWS CloudFormation template<a name="w22aac11c29c17d287c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.