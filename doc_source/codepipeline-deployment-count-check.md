# codepipeline\-deployment\-count\-check<a name="codepipeline-deployment-count-check"></a>

Checks whether the first deployment stage of the AWS Codepipeline performs more than one deployment\. Optionally checks if each of the subsequent remaining stages deploy to more than the specified number of deployments \(`deploymentLimit`\)\. 

**Identifier:** CODEPIPELINE\_DEPLOYMENT\_COUNT\_CHECK

**Resource Types:** AWS::CodePipeline::Pipeline

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific \(Mumbai\), Europe \(Paris\), US East \(Ohio\), Europe \(Ireland\), Europe \(Frankfurt\), South America \(Sao Paulo\), US East \(N\. Virginia\), Asia Pacific \(Seoul\), Europe \(London\), Asia Pacific \(Tokyo\), US West \(Oregon\), US West \(N\. California\), Asia Pacific \(Singapore\), Asia Pacific \(Sydney\), Canada \(Central\) Region

**Parameters:**

deploymentLimit \(Optional\)Type: int  
The maximum number of deployments each stage can perform\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d149c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.