# ecs\-fargate\-latest\-platform\-version<a name="ecs-fargate-latest-platform-version"></a>

Checks if Amazon Elastic Container Service \(ECS\) Fargate Services is running on the latest Fargate platform version\. The rule is NON\_COMPLIANT if ECS Service platformVersion not set to LATEST\. 

**Identifier:** ECS\_FARGATE\_LATEST\_PLATFORM\_VERSION

**Resource Types:** AWS::ECS::Service

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d243c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.