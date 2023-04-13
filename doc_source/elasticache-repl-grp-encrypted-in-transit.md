# elasticache\-repl\-grp\-encrypted\-in\-transit<a name="elasticache-repl-grp-encrypted-in-transit"></a>

Checks if Amazon ElastiCache replication groups have encryption\-in\-transit enabled\. The rule is NON\_COMPLIANT for an ElastiCache replication group if ‘TransitEncryptionEnabled’ is set to ‘false’\. 

**Identifier:** ELASTICACHE\_REPL\_GRP\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d301c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.