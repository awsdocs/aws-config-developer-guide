# cmk\-backing\-key\-rotation\-enabled<a name="cmk-backing-key-rotation-enabled"></a>

Checks if key rotation is enabled for each key and matches to the key ID of the customer created customer master key \(CMK\)\. The rule is COMPLIANT, if the key rotation is enabled for specific key object\. The rule is not applicable to CMKs that have imported key material\.

**Note**  
This rule only evaluates symmetric AWS KMS; keys and ignores asymmetric AWS KMS keys\.

**Identifier:** CMK\_BACKING\_KEY\_ROTATION\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7c77c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.