# elasticache\-repl\-grp\-redis\-auth\-enabled<a name="elasticache-repl-grp-redis-auth-enabled"></a>

Checks if Amazon ElastiCache replication groups have Redis AUTH enabled\. The rule is NON\_COMPLIANT for an ElastiCache replication group if the Redis version of its nodes is below 6 \(Version 6\+ use Redis ACLs\) and ‘AuthToken’ is missing or is empty/null\. 

**Identifier:** ELASTICACHE\_REPL\_GRP\_REDIS\_AUTH\_ENABLED

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d303c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.