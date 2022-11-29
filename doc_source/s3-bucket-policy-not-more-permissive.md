# s3\-bucket\-policy\-not\-more\-permissive<a name="s3-bucket-policy-not-more-permissive"></a>

Checks if your Amazon Simple Storage Service bucket policies do not allow other inter\-account permissions than the control Amazon S3 bucket policy that you provide\.

**Note**  
If you provide an invalid parameter value, you will see the following error: Value for controlPolicy parameter must be an Amazon S3 bucket policy\. 

**Identifier:** S3\_BUCKET\_POLICY\_NOT\_MORE\_PERMISSIVE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

controlPolicyType: String  
Amazon S3 bucket policy that defines an upper bound on the permissions of your S3 buckets\. The policy can be a maximum of 1024 characters long\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d489c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.