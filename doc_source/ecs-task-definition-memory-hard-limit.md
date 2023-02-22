# ecs\-task\-definition\-memory\-hard\-limit<a name="ecs-task-definition-memory-hard-limit"></a>

Checks if Amazon Elastic Container Service \(ECS\) task definitions have a set memory limit for its container definitions\. The rule is NON\_COMPLIANT for a task definition if the ‘memory’ parameter is absent for one container definition\. 

**Identifier:** ECS\_TASK\_DEFINITION\_MEMORY\_HARD\_LIMIT

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d249c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.