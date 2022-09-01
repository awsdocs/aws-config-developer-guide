# cloudformation\-stack\-drift\-detection\-check<a name="cloudformation-stack-drift-detection-check"></a>

Checks if the actual configuration of a Cloud Formation stack differs, or has drifted, from the expected configuration\. A stack is considered to have drifted if one or more of its resources differ from their expected configuration\. The rule and the stack are COMPLIANT when the stack drift status is IN\_SYNC\. The rule and the stack are NON\_COMPLIANT when the stack drift status is DRIFTED\.

**Identifier:** CLOUDFORMATION\_STACK\_DRIFT\_DETECTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Paris\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

cloudformationRoleArnType: String  
The AWS CloudFormation role ARN with IAM policy permissions to detect drift for AWS CloudFormation Stacks

## AWS CloudFormation template<a name="w85aac12c32c17b9c67c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.