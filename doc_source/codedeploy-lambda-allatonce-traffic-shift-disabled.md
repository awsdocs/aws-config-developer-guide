# codedeploy\-lambda\-allatonce\-traffic\-shift\-disabled<a name="codedeploy-lambda-allatonce-traffic-shift-disabled"></a>

Checks if the deployment group for Lambda Compute Platform is not using the default deployment configuration\. The rule is NON\_COMPLIANT if the deployment group is using the deployment configuration 'CodeDeployDefault\.LambdaAllAtOnce'\. 

**Identifier:** CODEDEPLOY\_LAMBDA\_ALLATONCE\_TRAFFIC\_SHIFT\_DISABLED

**Resource Types:** AWS::CodeDeploy::DeploymentGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d137c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.