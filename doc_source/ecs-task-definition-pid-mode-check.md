# ecs\-task\-definition\-pid\-mode\-check<a name="ecs-task-definition-pid-mode-check"></a>

Checks if ECSTaskDefinitions are configured to share a host’s process namespace with its Amazon Elastic Container Service \(Amazon ECS\) containers\. The rule is NON\_COMPLIANT if the pidMode parameter is set to ‘host’\. 

**Identifier:** ECS\_TASK\_DEFINITION\_PID\_MODE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w76aac11c31c17b7d215c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.