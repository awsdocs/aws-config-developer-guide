# iam\-policy\-no\-statements\-with\-full\-access<a name="iam-policy-no-statements-with-full-access"></a>

Checks if AWS Identity and Access Management \(IAM\) policies grant permissions to all actions on individual AWS resources\. The rule is NON\_COMPLIANT if the managed IAM policy allows full access to at least 1 AWS service\. 

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_FULL\_ACCESS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d221c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.