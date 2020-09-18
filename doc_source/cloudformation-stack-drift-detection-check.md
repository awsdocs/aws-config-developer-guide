# cloudformation\-stack\-drift\-detection\-check<a name="cloudformation-stack-drift-detection-check"></a>

Checks whether an AWS CloudFormation stack's actual configuration differs, or has drifted, from it's expected configuration\. A stack is considered to have drifted if one or more of its resources differ from their expected configuration\. The rule and the stack are COMPLIANT when the stack drift status is IN\_SYNC\. The rule and the stack are NON\_COMPLIANT when the stack drift status is DRIFTED\. 

**Note**  
If the stacks you created are not visible, choose Re\-evaluate and check again\.  
This rule depends on the DetectStackDrift API availability\. Based on the stack configuration, you may experience throttling\. AWS Config defaults the rule to NON\_COMPLIANT when there is throttling\.

**Identifier:** CLOUDFORMATION\_STACK\_DRIFT\_DETECTION\_CHECK

**Trigger type:** Configuration changes and periodic

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Europe \(Stockholm\), Europe \(Paris\), Middle East \(Bahrain\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 cloudformationRoleArn  
The AWS CloudFormation role ARN with IAM policy permissions to detect drift for AWS CloudFormation stacks\.  
If the role does not have all of the permissions, the rule fails\. The error appears as an annotation at the top of the page\. Ensure to attach `config.amazonaws.com` trusted permissions and `ReadOnlyAccess` policy permissions\. For specific policy permissions, refer to the [Detecting Unmanaged Configuration Changes to Stacks and Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) in the *AWS CloudFormation User Guide*\.

## AWS CloudFormation template<a name="w22aac11c29c17c37c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.