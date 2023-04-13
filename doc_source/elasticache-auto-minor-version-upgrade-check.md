# elasticache\-auto\-minor\-version\-upgrade\-check<a name="elasticache-auto-minor-version-upgrade-check"></a>

Checks if Amazon ElastiCache for Redis clusters have auto minor version upgrades enabled\. The rule is NON\_COMPLIANT for an ElastiCache cluster if it is using the Redis engine and 'AutoMinorVersionUpgrade' is not set to 'true'\. 

**Identifier:** ELASTICACHE\_AUTO\_MINOR\_VERSION\_UPGRADE\_CHECK

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d291c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.