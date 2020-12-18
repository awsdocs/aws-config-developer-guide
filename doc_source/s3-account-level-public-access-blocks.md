# s3\-account\-level\-public\-access\-blocks<a name="s3-account-level-public-access-blocks"></a>

Checks whether the required public access block settings are configured from account level\. The rule is only NON\_COMPLIANT when the fields set below do not match the corresponding fields in the configuration item\.

**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS

**Trigger type:** Configuration changes

**Note**  
This rule is only triggered by configuration changes for the specific region where the S3 endpoint is located\. In all other regions, the rule is checked periodically\. If a change was made in another region, there could be a delay before the rule returns NON\_COMPLIANT\. 

**AWS Region:** All supported AWS Regions except Middle East \(Bahrain\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

IgnorePublicAcls  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\. 

BlockPublicPolicy  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

BlockPublicAcls  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

RestrictPublicBuckets  
\(Optional\) Either enforced \(True\) or not \(False\)\. The default is True\.

## AWS CloudFormation template<a name="w24aac11c29c17d301c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.