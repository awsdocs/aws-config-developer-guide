# ecs\-task\-definition\-nonroot\-user<a name="ecs-task-definition-nonroot-user"></a>

Checks if ECSTaskDefinitions specify a user for Amazon Elastic Container Service \(Amazon ECS\) EC2 launch type containers to run on\. The rule is NON\_COMPLIANT if the ‘user’ parameter is not present or set to ‘root’\. 

**Identifier:** ECS\_TASK\_DEFINITION\_NONROOT\_USER

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w85aac12c32c17b9d243c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.