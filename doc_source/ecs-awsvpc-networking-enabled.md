# ecs\-awsvpc\-networking\-enabled<a name="ecs-awsvpc-networking-enabled"></a>

Checks if the networking mode for active ECSTaskDefinitions is set to ‘awsvpc’\. This rule is NON\_COMPLIANT if active ECSTaskDefinitions is not set to ‘awsvpc’\. 

**Identifier:** ECS\_AWSVPC\_NETWORKING\_ENABLED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d235c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.