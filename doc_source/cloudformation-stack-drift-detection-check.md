# cloudformation\-stack\-drift\-detection\-check<a name="cloudformation-stack-drift-detection-check"></a>

Checks whether your CloudFormation stacks' actual configuration differs, or has drifted, from its expected configuration\. 

**Identifier:** CLOUDFORMATION\_STACK\_DRIFT\_DETECTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Paris\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

cloudformationRoleArnType: String  
The AWS CloudFormation role ARN with IAM policy permissions to detect drift for AWS CloudFormation Stacks

## AWS CloudFormation template<a name="w29aac11c33c17b7c47c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.