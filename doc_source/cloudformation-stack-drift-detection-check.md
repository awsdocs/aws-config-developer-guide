# cloudformation\-stack\-drift\-detection\-check<a name="cloudformation-stack-drift-detection-check"></a>

Checks if the actual configuration of a Cloud Formation stack differs, or has drifted, from the expected configuration\. A stack is considered to have drifted if one or more of its resources differ from their expected configuration\. The rule and the stack are COMPLIANT when the stack drift status is IN\_SYNC\. The rule is NON\_COMPLIANT if the stack drift status is DRIFTED\.

**Identifier:** CLOUDFORMATION\_STACK\_DRIFT\_DETECTION\_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes and Periodic

**AWS Region:** Only available in Asia Pacific \(Mumbai\), US East \(Ohio\), Europe \(Ireland\), Europe \(Frankfurt\), South America \(Sao Paulo\), US East \(N\. Virginia\), Asia Pacific \(Seoul\), Europe \(London\), Asia Pacific \(Tokyo\), US West \(Oregon\), US West \(N\. California\), Asia Pacific \(Singapore\), Asia Pacific \(Sydney\), Canada \(Central\) Region

**Parameters:**

cloudformationRoleArnType: String  
The AWS CloudFormation role ARN with IAM policy permissions to detect drift for AWS CloudFormation Stacks

## AWS CloudFormation template<a name="w2aac12c33c15b9c79c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.