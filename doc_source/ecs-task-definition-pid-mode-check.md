# ecs\-task\-definition\-pid\-mode\-check<a name="ecs-task-definition-pid-mode-check"></a>

Checks if ECSTaskDefinitions are configured to share a host’s process namespace with its Amazon Elastic Container Service \(Amazon ECS\) containers\. The rule is NON\_COMPLIANT if the pidMode parameter is set to ‘host’\. 

**Identifier:** ECS\_TASK\_DEFINITION\_PID\_MODE\_CHECK

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d263c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.