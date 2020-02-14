# List of AWS Config Managed Rules<a name="managed-rules-by-aws-config"></a>

AWS Config currently supports the following managed rules in the compute; management and governance; network and content delivery; security, identity, and compliance; and storage categories\. This page also lists the rules that AWS Config does not currently support in the China \(Beijing\) and China \(Ningxia\) regions\.

## Analytics<a name="managed-rules-by-aws-config-analytics"></a>
+ [elasticache\-redis\-cluster\-automatic\-backup\-check](elasticache-redis-cluster-automatic-backup-check.md)
+ [elasticsearch\-encrypted\-at\-rest](elasticsearch-encrypted-at-rest.md)
+ [elasticsearch\-in\-vpc\-only](elasticsearch-in-vpc-only.md)

## Compute<a name="managed-rules-by-aws-config-compute"></a>
+ [approved\-amis\-by\-id](approved-amis-by-id.md)
+ [approved\-amis\-by\-tag](approved-amis-by-tag.md)
+ [autoscaling\-group\-elb\-healthcheck\-required](autoscaling-group-elb-healthcheck-required.md)
+ [desired\-instance\-tenancy](desired-instance-tenancy.md)
+ [desired\-instance\-type](desired-instance-type.md)
+ [ebs\-optimized\-instance](ebs-optimized-instance.md)
+ [ec2\-stopped\-instance](ec2-stopped-instance.md)
+ [ec2\-instance\-detailed\-monitoring\-enabled](ec2-instance-detailed-monitoring-enabled.md)
+ [ec2\-instance\-managed\-by\-systems\-manager](ec2-instance-managed-by-ssm.md)
+ [ec2\-instance\-no\-public\-ip](ec2-instance-no-public-ip.md)
+ [ec2\-instances\-in\-vpc](ec2-instances-in-vpc.md)
+ [ec2\-managedinstance\-applications\-blacklisted](ec2-managedinstance-applications-blacklisted.md)
+ [ec2\-managedinstance\-applications\-required](ec2-managedinstance-applications-required.md)
+ [ec2\-managedinstance\-association\-compliance\-status\-check](ec2-managedinstance-association-compliance-status-check.md)
+ [ec2\-managedinstance\-inventory\-blacklisted](ec2-managedinstance-inventory-blacklisted.md)
+ [ec2\-managedinstance\-patch\-compliance\-status\-check](ec2-managedinstance-patch-compliance-status-check.md)
+ [ec2\-managedinstance\-platform\-check](ec2-managedinstance-platform-check.md)
+ [ec2\-security\-group\-attached\-to\-eni](ec2-security-group-attached-to-eni.md)
+ [ec2\-volume\-inuse\-check](ec2-volume-inuse-check.md)
+ [eip\-attached](eip-attached.md)
+ [elb\-acm\-certificate\-required](elb-acm-certificate-required.md)
+ [elb\-custom\-security\-policy\-ssl\-check](elb-custom-security-policy-ssl-check.md)
+ [elb\-logging\-enabled](elb-logging-enabled.md)
+ [elb\-predefined\-security\-policy\-ssl\-check](elb-predefined-security-policy-ssl-check.md)
+ [encrypted\-volumes](encrypted-volumes.md)
+ [lambda\-concurrency\-check](lambda-concurrency-check.md)
+ [lambda\-dlq\-check](lambda-dlq-check.md)
+ [lambda\-function\-settings\-check](lambda-function-settings-check.md)
+ [lambda\-function\-public\-access\-prohibited](lambda-function-public-access-prohibited.md)\*
+ [lambda\-inside\-vpc](lambda-inside-vpc.md)
+ [restricted\-common\-ports](restricted-common-ports.md)
+ [restricted\-ssh](restricted-ssh.md)

## Cryptography and PKI<a name="managed-rules-by-aws-config-cryptographyandpki"></a>
+ [kms\-cmk\-not\-scheduled\-for\-deletion](kms-cmk-not-scheduled-for-deletion.md)

## Database<a name="managed-rules-by-aws-config-database"></a>
+ [db\-instance\-backup\-enabled](db-instance-backup-enabled.md)
+ [dynamodb\-autoscaling\-enabled](dynamodb-autoscaling-enabled.md)
+ [dynamodb\-table\-encryption\-enabled](dynamodb-table-encryption-enabled.md)
+ [dynamodb\-throughput\-limit\-check](dynamodb-throughput-limit-check.md)
+ [rds\-enhanced\-monitoring\-enabled](rds-enhanced-monitoring-enabled.md)
+ [rds\-instance\-public\-access\-check](rds-instance-public-access-check.md)
+ [rds\-multi\-az\-support](rds-multi-az-support.md)
+ [rds\-snapshots\-public\-prohibited](rds-snapshots-public-prohibited.md)
+ [rds\-storage\-encrypted](rds-storage-encrypted.md)
+ [redshift\-cluster\-configuration\-check](redshift-cluster-configuration-check.md)
+ [redshift\-cluster\-maintenancesettings\-check](redshift-cluster-maintenancesettings-check.md)
+ [redshift\-cluster\-public\-access\-check](redshift-cluster-public-access-check.md)

## Machine Learning<a name="managed-rules-by-aws-config-machinelearning"></a>
+ [sagemaker\-endpoint\-configuration\-kms\-key\-configured](sagemaker-endpoint-configuration-kms-key-configured.md)
+ [sagemaker\-notebook\-no\-direct\-internet\-access](sagemaker-notebook-no-direct-internet-access.md)
+ [sagemaker\-notebook\-kms\-configured](sagemaker-notebook-kms-configured.md)

## Management and Governance<a name="managed-rules-by-aws-config-managementandgovernance"></a>
+ [cloudformation\-stack\-drift\-detection\-check](cloudformation-stack-drift-detection-check.md)
+ [cloudformation\-stack\-notification\-check](cloudformation-stack-notification-check.md)
+ [cloud\-trail\-cloud\-watch\-logs\-enabled](cloud-trail-cloud-watch-logs-enabled.md)
+ [cloudtrail\-enabled](cloudtrail-enabled.md)
+ [cloud\-trail\-encryption\-enabled](cloud-trail-encryption-enabled.md)
+ [cloud\-trail\-log\-file\-validation\-enabled](cloud-trail-log-file-validation-enabled.md)
+ [cloudtrail\-s3\-dataevents\-enabled](cloudtrail-s3-dataevents-enabled.md)
+ [cloudwatch\-alarm\-action\-check](cloudwatch-alarm-action-check.md)
+ [cloudwatch\-alarm\-resource\-check](cloudwatch-alarm-resource-check.md)
+ [cloudwatch\-alarm\-settings\-check](cloudwatch-alarm-settings-check.md)
+ [cloudwatch\-log\-group\-encrypted](cloudwatch-log-group-encrypted.md)
+ [codebuild\-project\-envvar\-awscred\-check](codebuild-project-envvar-awscred-check.md)
+ [codebuild\-project\-source\-repo\-url\-check](codebuild-project-source-repo-url-check.md)
+ [codepipeline\-deployment\-count\-check](codepipeline-deployment-count-check.md)
+ [codepipeline\-region\-fanout\-check](codepipeline-region-fanout-check.md)
+ [multi\-region\-cloud\-trail\-enabled](multi-region-cloud-trail-enabled.md)
+ [required\-tags](required-tags.md)

## Migration and Transfer<a name="managed-rules-by-aws-config-migrationandtransfer"></a>
+ [dms\-replication\-not\-public](dms-replication-not-public.md)

## Network and Content Delivery<a name="managed-rules-by-aws-config-networkandcontentdelivery"></a>
+ [alb\-http\-to\-https\-redirection\-check](alb-http-to-https-redirection-check.md)
+ [api\-gw\-execution\-logging\-enabled](api-gw-execution-logging-enabled.md)
+ [api\-gw\-cache\-enabled\-and\-encrypted](api-gw-cache-enabled-and-encrypted.md)
+ [api\-gw\-endpoint\-type\-check](api-gw-endpoint-type-check.md)
+ [cloudfront\-viewer\-policy\-https](cloudfront-viewer-policy-https.md)
+ [internet\-gateway\-authorized\-vpc\-only](internet-gateway-authorized-vpc-only.md)
+ [service\-vpc\-endpoint\-enabled](service-vpc-endpoint-enabled.md)
+ [vpc\-default\-security\-group\-closed](vpc-default-security-group-closed.md)
+ [vpc\-flow\-logs\-enabled](vpc-flow-logs-enabled.md)
+ [vpc\-sg\-open\-only\-to\-authorized\-ports](vpc-sg-open-only-to-authorized-ports.md)
+ [vpc\-vpn\-2\-tunnels\-up](vpc-vpn-2-tunnels-up.md)

## Security, Identity & Compliance<a name="managed-rules-by-aws-config-security"></a>
+ [access\-keys\-rotated](access-keys-rotated.md)
+ [acm\-certificate\-expiration\-check](acm-certificate-expiration-check.md)
+ [cmk\-backing\-key\-rotation\-enabled](cmk-backing-key-rotation-enabled.md)
+ [fms\-security\-group\-audit\-policy\-check](fms-security-group-audit-policy-check.md)
+ [fms\-security\-group\-content\-check](fms-security-group-content-check.md)
+ [fms\-security\-group\-resource\-association\-check](fms-security-group-resource-association-check.md)
+ [fms\-shield\-resource\-policy\-check](fms-shield-resource-policy-check.md)
+ [fms\-webacl\-resource\-policy\-check](fms-webacl-resource-policy-check.md)
+ [fms\-webacl\-rulegroup\-association\-check](fms-webacl-rulegroup-association-check.md)
+ [guardduty\-non\-archived\-findings](guardduty-non-archived-findings.md)
+ [guardduty\-enabled\-centralized](guardduty-enabled-centralized.md)
+ [iam\-group\-has\-users\-check](iam-group-has-users-check.md)
+ [iam\-password\-policy](iam-password-policy.md)
+ [iam\-policy\-blacklisted\-check](iam-policy-blacklisted-check.md)
+ [iam\-policy\-in\-use](iam-policy-in-use.md)
+ [iam\-policy\-no\-statements\-with\-admin\-access](iam-policy-no-statements-with-admin-access.md)
+ [iam\-role\-managed\-policy\-check](iam-role-managed-policy-check.md)
+ [iam\-root\-access\-key\-check](iam-root-access-key-check.md)
+ [iam\-user\-group\-membership\-check](iam-user-group-membership-check.md)
+ [iam\-user\-mfa\-enabled](iam-user-mfa-enabled.md)
+ [iam\-user\-no\-policies\-check](iam-user-no-policies-check.md)
+ [iam\-user\-unused\-credentials\-check](iam-user-unused-credentials-check.md)
+ [mfa\-enabled\-for\-iam\-console\-access](mfa-enabled-for-iam-console-access.md)
+ [root\-account\-hardware\-mfa\-enabled](root-account-hardware-mfa-enabled.md)
+ [root\-account\-mfa\-enabled](root-account-mfa-enabled.md)
+ [shield\-advanced\-enabled\-autorenew](shield-advanced-enabled-autorenew.md)
+ [shield\-drt\-access](shield-drt-access.md)

## Storage<a name="managed-rules-by-aws-config-storage"></a>
+ [ebs\-snapshot\-public\-restorable\-check](ebs-snapshot-public-restorable-check.md)
+ [efs\-encrypted\-check](efs-encrypted-check.md)
+ [elb\-deletion\-protection\-enabled](elb-deletion-protection-enabled.md)
+ [emr\-master\-no\-public\-ip](emr-master-no-public-ip.md)
+ [emr\-kerberos\-enabled](emr-kerberos-enabled.md)
+ [s3\-account\-level\-public\-access\-blocks](s3-account-level-public-access-blocks.md)
+ [s3\-bucket\-blacklisted\-actions\-prohibited](s3-bucket-blacklisted-actions-prohibited.md)\*
+ [s3\-bucket\-logging\-enabled](s3-bucket-logging-enabled.md)
+ [s3\-bucket\-policy\-grantee\-check](s3-bucket-policy-grantee-check.md)\*
+ [s3\-bucket\-policy\-not\-more\-permissive](s3-bucket-policy-not-more-permissive.md)\*
+ [s3\-bucket\-public\-read\-prohibited](s3-bucket-public-read-prohibited.md)\*
+ [s3\-bucket\-public\-write\-prohibited](s3-bucket-public-write-prohibited.md)\*
+ [s3\-bucket\-replication\-enabled](s3-bucket-replication-enabled.md)
+ [s3\-bucket\-server\-side\-encryption\-enabled](s3-bucket-server-side-encryption-enabled.md)\*
+ [s3\-bucket\-ssl\-requests\-only](s3-bucket-ssl-requests-only.md)\*
+ [s3\-bucket\-versioning\-enabled](s3-bucket-versioning-enabled.md)

\*This rule uses automated reasoning tools \(ART\) to evaluate IAM permissions and resource policies for correctness\.

## Rules not Supported in China \(Beijing\) Region<a name="managed-rules-by-aws-config-BJS"></a>

AWS Config does not currently support the following rules in the Beijing region:
+ acm\-certificate\-expiration\-check
+ cmk\-backing\-key\-rotation\-enabled
+ cloud\-trail\-encryption\-enabled
+ cloud\-trail\-log\-file\-validation\-enabled
+ cloudformation\-stack\-drift\-detection\-check
+ codebuild\-project\-envvar\-awscred\-check 
+ codebuild\-project\-source\-repo\-url\-check 
+ codepipeline\-deployment\-count\-check
+ codepipeline\-region\-fanout\-check
+ elb\-acm\-certificate\-required 
+ encrypted\-volumes 
+ fms\-webacl\-resource\-policy\-check 
+ fms\-webacl\-rulegroup\-association\-check 
+ guardduty\-enabled\-centralized 
+ lambda\-function\-public\-access\-prohibited 
+ rds\-storage\-encrypted 
+ root\-account\-hardware\-mfa\-enabled
+ root\-account\-mfa\-enabled 
+ s3\-bucket\-blacklisted\-actions\-prohibited 
+ s3\-bucket\-policy\-grantee\-check
+ s3\-bucket\-policy\-not\-more\-permissive 
+ s3\-bucket\-public\-read\-prohibited 
+ s3\-bucket\-public\-write\-prohibited 
+ s3\-bucket\-server\-side\-encryption\-enabled 
+ s3\-bucket\-ssl\-requests\-only 

## Rules not Supported in China \(Ningxia\) Region<a name="managed-rules-by-aws-config-ZHY"></a>

All the rules that are not available in the Beijing region are also not available in the Ningxia region\. In addition to the above mentioned rules, AWS Config does not currently support the following rules in the Ningxia region:
+ lambda\-function\-settings\-check
+ cloudformation\-stack\-notification\-check
+ dynamodb\-table\-encryption\-enable