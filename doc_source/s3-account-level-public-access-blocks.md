# s3\-account\-level\-public\-access\-blocks<a name="s3-account-level-public-access-blocks"></a>

Checks if the required public access block settings are configured from account level\. The rule is only NON\_COMPLIANT when the fields set below do not match the corresponding fields in the configuration item\.

**Note**  
If you are using this rule, ensure that S3 Block Public Access is enabled\. The rule is change\-triggered, so it will not be invoked unless S3 Block Public Access is enabled\. If S3 Block Public Access is not enabled the rule returns INSUFFICIENT\_DATA\. This means that you still might have some public buckets\. For more information about setting up S3 Block Public Access, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)\.

**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS

**Trigger type:** Configuration changes \(current status not checked, only evaluted when changes generate new events\)

**Note**  
This rule is only triggered by configuration changes for the specific region where the S3 endpoint is located\. In all other regions, the rule is checked periodically\. If a change was made in another region, there could be a delay before the rule returns NON\_COMPLIANT\. 

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Middle East \(Bahrain\) Region

**Parameters:**

IgnorePublicAcls \(Optional\)Type: StringDefault: True  
IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy \(Optional\)Type: StringDefault: True  
BlockPublicPolicy is enforced or not, default True

BlockPublicAcls \(Optional\)Type: StringDefault: True  
BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets \(Optional\)Type: StringDefault: True  
RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template<a name="w29aac11c33c17b7d293c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.