# cmk\-backing\-key\-rotation\-enabled<a name="cmk-backing-key-rotation-enabled"></a>

Checks that key rotation is enabled for each customer master key \(CMK\)\. The rule is COMPLIANT, if the key rotation is enabled for specific key object\. The rule is not applicable to CMKs that have imported key material\.

**Identifier:** CMK\_BACKING\_KEY\_ROTATION\_ENABLED

**Trigger type:** Periodic

**Parameters:**

 None  

## AWS CloudFormation template<a name="w4aac13c29c17c75c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.