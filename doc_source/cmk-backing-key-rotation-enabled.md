# cmk\-backing\-key\-rotation\-enabled<a name="cmk-backing-key-rotation-enabled"></a>

Checks if automatic key rotation is enabled for each key and matches to the key ID of the customer created AWS KMS key\. The rule is NON\_COMPLIANT if the AWS Config recorder role for a resource does not have the kms:DescribeKey permission\. 

**Note**  
Automatic key rotation is not supported for asymmetric KMS keys, HMAC KMS keys, KMS keys with imported key material, or KMS keys in custom key stores\.

**Identifier:** CMK\_BACKING\_KEY\_ROTATION\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d129c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.