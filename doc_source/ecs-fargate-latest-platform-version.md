# ecs\-fargate\-latest\-platform\-version<a name="ecs-fargate-latest-platform-version"></a>

Checks if ECS Fargate services is set to the latest platform version\. The rule is NON\_COMPLIANT if PlatformVersion for the Fargate launch type is not set to LATEST, or if neither latestLinuxVersion nor `latestWindowsVersion` are provided as parameters\. 

**Identifier:** ECS\_FARGATE\_LATEST\_PLATFORM\_VERSION

**Resource Types:** AWS::ECS::Service

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

latestLinuxVersion \(Optional\)Type: String  
Latest Linux supported 'PlatformVersion' in semantic versioning \(SemVer\) format\. Parameter may be needed if Fargate was deployed and the 'PlatformVersion' was explicitly specified or CodeDeploy is used as the 'DeploymentController'

latestWindowsVersion \(Optional\)Type: String  
Latest Windows supported 'PlatformVersion' in semantic versioning \(SemVer\) format\. Parameter may be needed if Fargate was deployed and the 'PlatformVersion' was explicitly specified or CodeDeploy is used as the 'DeploymentController'

## AWS CloudFormation template<a name="w2aac12c33c15b9d253c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.