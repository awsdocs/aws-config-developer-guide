# Operational Best Practices for NIST CSF<a name="operational-best-practices-for-nist-csf"></a>

Conformance packs provide a general\-purpose compliance framework designed to enable you to create security, operational or cost\-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions\. Conformance Packs, as sample templates, are not designed to fully ensure compliance with a specific governance or compliance standard\. You are responsible for making your own assessment of whether your use of the Services meets applicable legal and regulatory requirements\.

The following provides a sample mapping between the NIST Cyber Security Framework \(CSF\) and AWS managed Config rules\. Each AWS Config rule applies to a specific AWS resource, and relates to one or more NIST CSF controls\. A NIST CSF control can be related to multiple Config rules\. Refer to the table below for more detail and guidance related to these mappings\.

This Conformance Pack was validated by AWS Security Assurance Services LLC \(AWS SAS\), which is a team of Payment Card Industry Qualified Security Assessors \(QSAs\), HITRUST Certified Common Security Framework Practitioners \(CCSFPs\), and compliance professionals certified to provide guidance and assessments for various industry frameworks\. AWS SAS professionals designed this Conformance Pack to enable you to align to a subset of the NIST CSF\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-nist-csf.html)

## Template<a name="nist-csf-conformance-pack-sample"></a>

```
##################################################################################
#                                                                                 
#   Conformance Pack:                                                             
#     Operational Best Practices for NIST CSF                                   
#                                                                                 
#   This conformance pack helps verify compliance with NIST CSF requirements.   
#                                                                                 
#   See Parameters section for names and descriptions of required parameters.     
#                                                                                 
##################################################################################

Conditions:
  accessKeysRotatedParamMaxAccessKeyAge:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: AccessKeysRotatedParamMaxAccessKeyAge
  acmCertificateExpirationCheckParamDaysToExpiration:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: AcmCertificateExpirationCheckParamDaysToExpiration
  guarddutyNonArchivedFindingsParamDaysHighSev:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: GuarddutyNonArchivedFindingsParamDaysHighSev
  guarddutyNonArchivedFindingsParamDaysLowSev:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: GuarddutyNonArchivedFindingsParamDaysLowSev
  guarddutyNonArchivedFindingsParamDaysMediumSev:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: GuarddutyNonArchivedFindingsParamDaysMediumSev
  iamPasswordPolicyParamMaxPasswordAge:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamMaxPasswordAge
  iamPasswordPolicyParamMinimumPasswordLength:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamMinimumPasswordLength
  iamPasswordPolicyParamPasswordReusePrevention:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamPasswordReusePrevention
  iamPasswordPolicyParamRequireLowercaseCharacters:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamRequireLowercaseCharacters
  iamPasswordPolicyParamRequireNumbers:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamRequireNumbers
  iamPasswordPolicyParamRequireSymbols:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamRequireSymbols
  iamPasswordPolicyParamRequireUppercaseCharacters:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamPasswordPolicyParamRequireUppercaseCharacters
  iamUserUnusedCredentialsCheckParamMaxCredentialUsageAge:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: IamUserUnusedCredentialsCheckParamMaxCredentialUsageAge
  restrictedIncomingTrafficParamBlockedPort1:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: RestrictedIncomingTrafficParamBlockedPort1
  restrictedIncomingTrafficParamBlockedPort2:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: RestrictedIncomingTrafficParamBlockedPort2
  restrictedIncomingTrafficParamBlockedPort3:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: RestrictedIncomingTrafficParamBlockedPort3
  restrictedIncomingTrafficParamBlockedPort4:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: RestrictedIncomingTrafficParamBlockedPort4
  restrictedIncomingTrafficParamBlockedPort5:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: RestrictedIncomingTrafficParamBlockedPort5
  s3AccountLevelPublicAccessBlocksParamBlockPublicAcls:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: S3AccountLevelPublicAccessBlocksParamBlockPublicAcls
  s3AccountLevelPublicAccessBlocksParamBlockPublicPolicy:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: S3AccountLevelPublicAccessBlocksParamBlockPublicPolicy
  s3AccountLevelPublicAccessBlocksParamIgnorePublicAcls:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: S3AccountLevelPublicAccessBlocksParamIgnorePublicAcls
  s3AccountLevelPublicAccessBlocksParamRestrictPublicBuckets:
    Fn::Not:
    - Fn::Equals:
      - ''
      - Ref: S3AccountLevelPublicAccessBlocksParamRestrictPublicBuckets
Parameters:
  AccessKeysRotatedParamMaxAccessKeyAge:
    Default: '90'
    Description: Maximum number of days without rotation. Default 90.
    Type: String
  AcmCertificateExpirationCheckParamDaysToExpiration:
    Default: '90'
    Description: Specify the number of days before the rule flags the ACM Certificate
      as noncompliant.
    Type: String
  GuarddutyNonArchivedFindingsParamDaysHighSev:
    Default: '1'
    Description: The number of days Amazon GuardDuty high severity findings are allowed
      to stay non archived. The default is 1 day.
    Type: String
  GuarddutyNonArchivedFindingsParamDaysLowSev:
    Default: '30'
    Description: The number of days Amazon GuardDuty low severity findings are allowed
      to stay non archived. The default is 30 days.
    Type: String
  GuarddutyNonArchivedFindingsParamDaysMediumSev:
    Default: '7'
    Description: The number of days Amazon GuardDuty medium severity findings are
      allowed to stay non archived. The default is 7 days.
    Type: String
  IamPasswordPolicyParamMaxPasswordAge:
    Default: '90'
    Description: Number of days before password expiration.
    Type: String
  IamPasswordPolicyParamMinimumPasswordLength:
    Default: '14'
    Description: Password minimum length.
    Type: String
  IamPasswordPolicyParamPasswordReusePrevention:
    Default: '24'
    Description: Number of passwords before allowing reuse.
    Type: String
  IamPasswordPolicyParamRequireLowercaseCharacters:
    Default: 'TRUE'
    Description: Require at least one lowercase character in password.
    Type: String
  IamPasswordPolicyParamRequireNumbers:
    Default: 'TRUE'
    Description: Require at least one number in password.
    Type: String
  IamPasswordPolicyParamRequireSymbols:
    Default: 'TRUE'
    Description: Require at least one symbol in password.
    Type: String
  IamPasswordPolicyParamRequireUppercaseCharacters:
    Default: 'TRUE'
    Description: Require at least one uppercase character in password.
    Type: String
  IamUserUnusedCredentialsCheckParamMaxCredentialUsageAge:
    Default: '90'
    Description: Maximum number of days a credential cannot be used. The default value
      is 90 days.
    Type: String
  RestrictedIncomingTrafficParamBlockedPort1:
    Default: '20'
    Description: Blocked TCP port number.
    Type: String
  RestrictedIncomingTrafficParamBlockedPort2:
    Default: '21'
    Description: Blocked TCP port number.
    Type: String
  RestrictedIncomingTrafficParamBlockedPort3:
    Default: '3389'
    Description: Blocked TCP port number.
    Type: String
  RestrictedIncomingTrafficParamBlockedPort4:
    Default: '3306'
    Description: Blocked TCP port number.
    Type: String
  RestrictedIncomingTrafficParamBlockedPort5:
    Default: '4333'
    Description: Blocked TCP port number.
    Type: String
  S3AccountLevelPublicAccessBlocksParamBlockPublicAcls:
    Default: 'TRUE'
    Description: BlockPublicAcls is enforced or not, default True
    Type: String
  S3AccountLevelPublicAccessBlocksParamBlockPublicPolicy:
    Default: 'TRUE'
    Description: BlockPublicPolicy is enforced or not, default True
    Type: String
  S3AccountLevelPublicAccessBlocksParamIgnorePublicAcls:
    Default: 'TRUE'
    Description: IgnorePublicAcls is enforced or not, default True
    Type: String
  S3AccountLevelPublicAccessBlocksParamRestrictPublicBuckets:
    Default: 'TRUE'
    Description: RestrictPublicBuckets is enforced or not, default True
    Type: String
Resources:
  AccessKeysRotated:
    Controls:
    - PR.AC-1
    Properties:
      ConfigRuleName: access-keys-rotated
      Description: Checks whether the active access keys are rotated within the number
        of days specified in maxAccessKeyAge. The rule is non-compliant if the access
        keys have not been rotated for more than maxAccessKeyAge number of days.
      InputParameters:
        maxAccessKeyAge:
          Fn::If:
          - accessKeysRotatedParamMaxAccessKeyAge
          - Ref: AccessKeysRotatedParamMaxAccessKeyAge
          - Ref: AWS::NoValue
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ACCESS_KEYS_ROTATED
    Type: AWS::Config::ConfigRule
  AcmCertificateExpirationCheck:
    Controls:
    - PR.AC-5
    Properties:
      ConfigRuleName: acm-certificate-expiration-check
      Description: Checks whether ACM Certificates in your account are marked for
        expiration within the specified number of days. Certificates provided by ACM
        are automatically renewed. ACM does not automatically renew certificates that
        you import.
      InputParameters:
        daysToExpiration:
          Fn::If:
          - acmCertificateExpirationCheckParamDaysToExpiration
          - Ref: AcmCertificateExpirationCheckParamDaysToExpiration
          - Ref: AWS::NoValue
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes:
        - AWS::ACM::Certificate
      Source:
        Owner: AWS
        SourceIdentifier: ACM_CERTIFICATE_EXPIRATION_CHECK
    Type: AWS::Config::ConfigRule
  AlbHttpToHttpsRedirectionCheck:
    Controls:
    - PR.DS-2
    Properties:
      ConfigRuleName: alb-http-to-https-redirection-check
      Description: Checks whether HTTP to HTTPS redirection is configured on all HTTP
        listeners of Application Load Balancers. The rule is NON_COMPLIANT if one
        or more HTTP listeners of Application Load Balancer do not have HTTP to HTTPS
        redirection configured.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK
    Type: AWS::Config::ConfigRule
  ApiGwCacheEnabledAndEncrypted:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: api-gw-cache-enabled-and-encrypted
      Description: Checks that all methods in Amazon API Gateway stages have cache
        enabled and cache encrypted. The rule is NON_COMPLIANT if any method in Amazon
        API Gateway stage is not configured to cache or the cache is not encrypted.
      Scope:
        ComplianceResourceTypes:
        - AWS::ApiGateway::Stage
      Source:
        Owner: AWS
        SourceIdentifier: API_GW_CACHE_ENABLED_AND_ENCRYPTED
    Type: AWS::Config::ConfigRule
  ApiGwExecutionLoggingEnabled:
    Controls:
    - ID.AM-3
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.CM-1
    - DE.CM-7
    Properties:
      ConfigRuleName: api-gw-execution-logging-enabled
      Description: Checks that all methods in Amazon API Gateway stage has logging
        enabled. The rule is NON_COMPLIANT if logging is not enabled. The rule is
        NON_COMPLIANT if loggingLevel is neither ERROR nor INFO.
      Scope:
        ComplianceResourceTypes:
        - AWS::ApiGateway::Stage
        - AWS::ApiGatewayV2::Stage
      Source:
        Owner: AWS
        SourceIdentifier: API_GW_EXECUTION_LOGGING_ENABLED
    Type: AWS::Config::ConfigRule
  AutoscalingGroupElbHealthcheckRequired:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.PT-5
    Properties:
      ConfigRuleName: autoscaling-group-elb-healthcheck-required
      Description: Checks whether your Auto Scaling groups that are associated with
        a load balancer are using Elastic Load Balancing health checks.
      Scope:
        ComplianceResourceTypes:
        - AWS::AutoScaling::AutoScalingGroup
      Source:
        Owner: AWS
        SourceIdentifier: AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED
    Type: AWS::Config::ConfigRule
  CloudTrailCloudWatchLogsEnabled:
    Controls:
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    Properties:
      ConfigRuleName: cloud-trail-cloud-watch-logs-enabled
      Description: Checks whether AWS CloudTrail trails are configured to send logs
        to Amazon CloudWatch logs. The trail is non-compliant if the CloudWatchLogsLogGroupArn
        property of the trail is empty.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED
    Type: AWS::Config::ConfigRule
  CloudTrailEnabled:
    Controls:
    - ID.AM-3
    - PR.AC-6
    - PR.DS-5
    - PR.MA-2
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-6
    - DE.CM-7
    Properties:
      ConfigRuleName: cloudtrail-enabled
      Description: Checks whether AWS CloudTrail is enabled in your AWS account.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUD_TRAIL_ENABLED
    Type: AWS::Config::ConfigRule
  CloudTrailEncryptionEnabled:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: cloud-trail-encryption-enabled
      Description: Checks whether AWS CloudTrail is configured to use the server side
        encryption (SSE) AWS Key Management Service (AWS KMS) customer master key
        (CMK) encryption. The rule is compliant if the KmsKeyId is defined.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUD_TRAIL_ENCRYPTION_ENABLED
    Type: AWS::Config::ConfigRule
  CloudTrailLogFileValidationEnabled:
    Controls:
    - PR.DS-6
    Properties:
      ConfigRuleName: cloud-trail-log-file-validation-enabled
      Description: Checks whether AWS CloudTrail creates a signed digest file with
        logs. AWS recommends that the file validation must be enabled on all trails.
        The rule is noncompliant if the validation is not enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED
    Type: AWS::Config::ConfigRule
  CloudformationStackNotificationCheck:
    Controls:
    - DE.DP-4
    Properties:
      ConfigRuleName: cloudformation-stack-notification-check
      Description: Checks whether your CloudFormation stacks are sending event notifications
        to an SNS topic. Optionally checks whether specified SNS topics are used.
      Scope:
        ComplianceResourceTypes:
        - AWS::CloudFormation::Stack
      Source:
        Owner: AWS
        SourceIdentifier: CLOUDFORMATION_STACK_NOTIFICATION_CHECK
    Type: AWS::Config::ConfigRule
  CloudtrailS3DataeventsEnabled:
    Controls:
    - PR.DS-5
    - DE.AE-3
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-6
    - DE.CM-7
    Properties:
      ConfigRuleName: cloudtrail-s3-dataevents-enabled
      Description: Checks whether at least one AWS CloudTrail trail is logging Amazon
        S3 data events for all S3 buckets. The rule is NON_COMPLIANT if trails log
        data events for S3 buckets is not configured.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUDTRAIL_S3_DATAEVENTS_ENABLED
    Type: AWS::Config::ConfigRule
  CloudwatchAlarmActionCheck:
    Controls:
    - DE.AE-5
    Properties:
      ConfigRuleName: cloudwatch-alarm-action-check
      Description: Checks whether CloudWatch alarms have at least one alarm action,
        one INSUFFICIENT_DATA action, or one OK action enabled. Optionally, checks
        whether any of the actions matches one of the specified ARNs.
      InputParameters:
        alarmActionRequired: 'TRUE'
        insufficientDataActionRequired: 'TRUE'
        okActionRequired: 'FALSE'
      Scope:
        ComplianceResourceTypes:
        - AWS::CloudWatch::Alarm
      Source:
        Owner: AWS
        SourceIdentifier: CLOUDWATCH_ALARM_ACTION_CHECK
    Type: AWS::Config::ConfigRule
  CloudwatchLogGroupEncrypted:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: cloudwatch-log-group-encrypted
      Description: Checks whether a log group in Amazon CloudWatch Logs is encrypted.
        The rule is NON_COMPLIANT if CloudWatch Logs has log group without encryption
        enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: CLOUDWATCH_LOG_GROUP_ENCRYPTED
    Type: AWS::Config::ConfigRule
  CodebuildProjectEnvvarAwscredCheck:
    Controls:
    - PR.DS-5
    Properties:
      ConfigRuleName: codebuild-project-envvar-awscred-check
      Description: Checks whether the project contains environment variables AWS_ACCESS_KEY_ID
        and AWS_SECRET_ACCESS_KEY. The rule is NON_COMPLIANT when the project environment
        variables contains plaintext credentials.
      Scope:
        ComplianceResourceTypes:
        - AWS::CodeBuild::Project
      Source:
        Owner: AWS
        SourceIdentifier: CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK
    Type: AWS::Config::ConfigRule
  CodebuildProjectSourceRepoUrlCheck:
    Controls:
    - DE.AE-5
    Properties:
      ConfigRuleName: codebuild-project-source-repo-url-check
      Description: Checks whether the GitHub or Bitbucket source repository URL contains
        either personal access tokens or user name and password. The rule is complaint
        with the usage of OAuth to grant authorization for accessing GitHub or Bitbucket
        repositories.
      Scope:
        ComplianceResourceTypes:
        - AWS::CodeBuild::Project
      Source:
        Owner: AWS
        SourceIdentifier: CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK
    Type: AWS::Config::ConfigRule
  CodepipelineDeploymentCountCheck:
    Controls:
    - PR.IP-2
    - DE.CM-7
    Properties:
      ConfigRuleName: codepipeline-deployment-count-check
      Description: Checks whether the first deployment stage of the AWS Codepipeline
        performs more than one deployment. Optionally checks if each of the subsequent
        remaining stages deploy to more than the specified number of deployments (deploymentLimit).
      Scope:
        ComplianceResourceTypes:
        - AWS::CodePipeline::Pipeline
      Source:
        Owner: AWS
        SourceIdentifier: CODEPIPELINE_DEPLOYMENT_COUNT_CHECK
    Type: AWS::Config::ConfigRule
  CodepipelineRegionFanoutCheck:
    Controls:
    - PR.IP-2
    - DE.CM-7
    Properties:
      ConfigRuleName: codepipeline-region-fanout-check
      Description: Checks whether each stage in the AWS CodePipeline deploys to more
        regions than N times the number of regions the pipeline has deployed to in
        all previous stages, where N is regionFanoutFactor. The first deployment stage
        can deploy to only one region.
      Scope:
        ComplianceResourceTypes:
        - AWS::CodePipeline::Pipeline
      Source:
        Owner: AWS
        SourceIdentifier: CODEPIPELINE_REGION_FANOUT_CHECK
    Type: AWS::Config::ConfigRule
  DbInstanceBackupEnabled:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.IP-4
    - PR.PT-5
    Properties:
      ConfigRuleName: db-instance-backup-enabled
      Description: Checks whether RDS DB instances have backups enabled.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBInstance
      Source:
        Owner: AWS
        SourceIdentifier: DB_INSTANCE_BACKUP_ENABLED
    Type: AWS::Config::ConfigRule
  DmsReplicationNotPublic:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: dms-replication-not-public
      Description: Checks whether AWS Database Migration Service replication instances
        are public. The rule is NON_COMPLIANT if PubliclyAccessible field is True.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes: []
      Source:
        Owner: AWS
        SourceIdentifier: DMS_REPLICATION_NOT_PUBLIC
    Type: AWS::Config::ConfigRule
  DynamodbAutoscalingEnabled:
    Controls:
    - ID.BE-5
    Properties:
      ConfigRuleName: dynamodb-autoscaling-enabled
      Description: This rule checks whether Auto Scaling is enabled on your DynamoDB
        tables. Optionally you can set the read and write capacity units for the table.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes:
        - AWS::DynamoDB::Table
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_AUTOSCALING_ENABLED
    Type: AWS::Config::ConfigRule
  DynamodbPitrEnabled:
    Controls:
    - PR.IP-4
    Properties:
      ConfigRuleName: dynamodb-pitr-enabled
      Description: Check that point in time recovery is enabled for Amazon DynamoDB
        tables.
      Scope:
        ComplianceResourceTypes:
        - AWS::DynamoDB::Table
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_PITR_ENABLED
    Type: AWS::Config::ConfigRule
  DynamodbThroughputLimitCheck:
    Controls:
    - ID.BE-5
    - PR.DS-4
    Properties:
      ConfigRuleName: dynamodb-throughput-limit-check
      Description: Checks whether provisioned DynamoDB throughput is approaching the
        maximum limit for your account.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_THROUGHPUT_LIMIT_CHECK
    Type: AWS::Config::ConfigRule
  EbsOptimizedInstance:
    Controls:
    - PR.IP-7
    Properties:
      ConfigRuleName: ebs-optimized-instance
      Description: Checks whether EBS optimization is enabled for your EC2 instances
        that can be EBS-optimized.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Instance
      Source:
        Owner: AWS
        SourceIdentifier: EBS_OPTIMIZED_INSTANCE
    Type: AWS::Config::ConfigRule
  EbsSnapshotPublicRestorableCheck:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: ebs-snapshot-public-restorable-check
      Description: Checks whether Amazon Elastic Block Store (Amazon EBS) snapshots
        are not publicly restorable. The rule is NON_COMPLIANT if one or more snapshots
        with RestorableByUserIds field are set to all, that is, Amazon EBS snapshots
        are public.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK
    Type: AWS::Config::ConfigRule
  Ec2InstanceDetailedMonitoringEnabled:
    Controls:
    - DE.DP-5
    Properties:
      ConfigRuleName: ec2-instance-detailed-monitoring-enabled
      Description: Checks whether detailed monitoring is enabled for EC2 instances.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Instance
      Source:
        Owner: AWS
        SourceIdentifier: EC2_INSTANCE_DETAILED_MONITORING_ENABLED
    Type: AWS::Config::ConfigRule
  Ec2InstanceManagedBySsm:
    Controls:
    - ID.AM-2
    - PR.DS-3
    - PR.IP-1
    Properties:
      ConfigRuleName: ec2-instance-managed-by-systems-manager
      Description: Checks whether the Amazon EC2 instances in your account are managed
        by AWS Systems Manager.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Instance
        - AWS::SSM::ManagedInstanceInventory
      Source:
        Owner: AWS
        SourceIdentifier: EC2_INSTANCE_MANAGED_BY_SSM
    Type: AWS::Config::ConfigRule
  Ec2InstanceNoPublicIp:
    Controls:
    - PR.AC-3
    - PR.AC-5
    Properties:
      ConfigRuleName: ec2-instance-no-public-ip
      Description: Checks whether Amazon Elastic Compute Cloud (Amazon EC2) instances
        have a public IP association. The rule is NON_COMPLIANT if the publicIp field
        is present in the Amazon EC2 instance configuration item. This rule applies
        only to IPv4.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Instance
      Source:
        Owner: AWS
        SourceIdentifier: EC2_INSTANCE_NO_PUBLIC_IP
    Type: AWS::Config::ConfigRule
  Ec2ManagedinstanceAssociationComplianceStatusCheck:
    Controls:
    - ID.AM-2
    - PR.DS-3
    - PR.IP-1
    Properties:
      ConfigRuleName: ec2-managedinstance-association-compliance-status-check
      Description: Checks whether the compliance status of the AWS Systems Manager
        association compliance is COMPLIANT or NON_COMPLIANT after the association
        execution on the instance. The rule is compliant if the field status is COMPLIANT.
      Scope:
        ComplianceResourceTypes:
        - AWS::SSM::AssociationCompliance
      Source:
        Owner: AWS
        SourceIdentifier: EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK
    Type: AWS::Config::ConfigRule
  Ec2ManagedinstancePatchComplianceStatusCheck:
    Controls:
    - ID.RA-1
    Properties:
      ConfigRuleName: ec2-managedinstance-patch-compliance-status-check
      Description: Checks whether the compliance status of the AWS Systems Manager
        patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation
        on the instance. The rule is compliant if the field status is COMPLIANT.
      Scope:
        ComplianceResourceTypes:
        - AWS::SSM::PatchCompliance
      Source:
        Owner: AWS
        SourceIdentifier: EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK
    Type: AWS::Config::ConfigRule
  Ec2SecurityGroupAttachedToEni:
    Controls:
    - PR.DS-3
    Properties:
      ConfigRuleName: ec2-security-group-attached-to-eni
      Description: 'Checks that non-default security groups are attached to Amazon
        Elastic Compute Cloud (EC2) instances or an elastic network interfaces (ENIs).
        The rule returns NON_COMPLIANT if the security group is not associated with
        an EC2 instance or an ENI. '
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::SecurityGroup
      Source:
        Owner: AWS
        SourceIdentifier: EC2_SECURITY_GROUP_ATTACHED_TO_ENI
    Type: AWS::Config::ConfigRule
  Ec2StoppedInstance:
    Controls:
    - PR.IP-1
    Properties:
      ConfigRuleName: ec2-stopped-instance
      Description: Checks whether there are instances stopped for more than the allowed
        number of days.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: EC2_STOPPED_INSTANCE
    Type: AWS::Config::ConfigRule
  Ec2VolumeInuseCheck:
    Controls:
    - PR.IP-1
    Properties:
      ConfigRuleName: ec2-volume-inuse-check
      Description: Checks whether EBS volumes are attached to EC2 instances.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Volume
      Source:
        Owner: AWS
        SourceIdentifier: EC2_VOLUME_INUSE_CHECK
    Type: AWS::Config::ConfigRule
  EfsEncryptedCheck:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: efs-encrypted-check
      Description: Checks whether Amazon EFS are configured to encrypt file data using
        AWS KMS. The rule is NON_COMPLIANT if the Encrypted key is set to False on
        DescribeFileSystems or, if specified, KmsKeyId key on DescribeFileSystems
        is not matching KmsKeyId parameter.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: EFS_ENCRYPTED_CHECK
    Type: AWS::Config::ConfigRule
  EipAttached:
    Controls:
    - PR.DS-3
    Properties:
      ConfigRuleName: eip-attached
      Description: Checks whether all EIP addresses allocated to a VPC are attached
        to EC2 instances or in-use ENIs.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::EIP
      Source:
        Owner: AWS
        SourceIdentifier: EIP_ATTACHED
    Type: AWS::Config::ConfigRule
  ElasticacheRedisClusterAutomaticBackupCheck:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.IP-4
    - PR.PT-5
    Properties:
      ConfigRuleName: elasticache-redis-cluster-automatic-backup-check
      Description: The rule is NON_COMPLIANT if SnapshotRetentionLimit for Redis cluster
        is less than the SnapshotRetentionPeriod parameter, i.e from 0 to 15 as the
        default is 15.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK
    Type: AWS::Config::ConfigRule
  ElasticsearchEncryptedAtRest:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: elasticsearch-encrypted-at-rest
      Description: Checks whether Amazon Elasticsearch Service (Amazon ES) domains
        have encryption at rest configuration enabled. The rule is NON_COMPLIANT if
        EncryptionAtRestOptions field is not enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ELASTICSEARCH_ENCRYPTED_AT_REST
    Type: AWS::Config::ConfigRule
  ElasticsearchInVpcOnly:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    Properties:
      ConfigRuleName: elasticsearch-in-vpc-only
      Description: Checks whether Amazon Elasticsearch Service domains are in Amazon
        Virtual Private Cloud (VPC). The rule is NON_COMPLIANT if ElasticSearch Service
        domain endpoint is public.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ELASTICSEARCH_IN_VPC_ONLY
    Type: AWS::Config::ConfigRule
  ElbAcmCertificateRequired:
    Controls:
    - PR.DS-2
    Properties:
      ConfigRuleName: elb-acm-certificate-required
      Description: This rule checks whether the Elastic Load Balancer(s) uses SSL
        certificates provided by AWS Certificate Manager. You must use an SSL or HTTPS
        listener with your Elastic Load Balancer to use this rule.
      Scope:
        ComplianceResourceTypes:
        - AWS::ElasticLoadBalancing::LoadBalancer
      Source:
        Owner: AWS
        SourceIdentifier: ELB_ACM_CERTIFICATE_REQUIRED
    Type: AWS::Config::ConfigRule
  ElbDeletionProtectionEnabled:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.IP-3
    - PR.PT-5
    Properties:
      ConfigRuleName: elb-deletion-protection-enabled
      Description: Checks whether an Elastic Load Balancer has deletion protection
        enabled. The rule is NON_COMPLIANT if deletion_protection.enabled is false.
      Scope:
        ComplianceResourceTypes:
        - AWS::ElasticLoadBalancingV2::LoadBalancer
      Source:
        Owner: AWS
        SourceIdentifier: ELB_DELETION_PROTECTION_ENABLED
    Type: AWS::Config::ConfigRule
  ElbLoggingEnabled:
    Controls:
    - ID.AM-3
    - PR.DS-5
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.AE-4
    - DE.CM-1
    - DE.CM-7
    Properties:
      ConfigRuleName: elb-logging-enabled
      Description: Checks whether the Application Load Balancers and the Classic Load
        Balancers have logging enabled.
      Scope:
        ComplianceResourceTypes:
        - AWS::ElasticLoadBalancing::LoadBalancer
        - AWS::ElasticLoadBalancingV2::LoadBalancer
      Source:
        Owner: AWS
        SourceIdentifier: ELB_LOGGING_ENABLED
    Type: AWS::Config::ConfigRule
  EmrKerberosEnabled:
    Controls:
    - PR.AC-4
    - PR.AC-6
    Properties:
      ConfigRuleName: emr-kerberos-enabled
      Description: The rule is NON_COMPLIANT if a security configuration is not attached
        to the cluster or the security configuration does not satisfy the specified
        rule parameters.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: EMR_KERBEROS_ENABLED
    Type: AWS::Config::ConfigRule
  EmrMasterNoPublicIp:
    Controls:
    - PR.AC-3
    - PR.AC-5
    Properties:
      ConfigRuleName: emr-master-no-public-ip
      Description: Checks whether Amazon Elastic MapReduce (EMR) clusters' master
        nodes have public IPs. The rule is NON_COMPLIANT if the master node has a
        public IP.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes: []
      Source:
        Owner: AWS
        SourceIdentifier: EMR_MASTER_NO_PUBLIC_IP
    Type: AWS::Config::ConfigRule
  EncryptedVolumes:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: encrypted-volumes
      Description: Checks whether EBS volumes that are in an attached state are encrypted.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Volume
      Source:
        Owner: AWS
        SourceIdentifier: ENCRYPTED_VOLUMES
    Type: AWS::Config::ConfigRule
  GuarddutyEnabledCentralized:
    Controls:
    - ID.RA-1
    - ID.RA-2
    - ID.RA-3
    - PR.DS-5
    - DE.AE-2
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-4
    - DE.CM-6
    - DE.CM-7
    - DE.DP-4
    Properties:
      ConfigRuleName: guardduty-enabled-centralized
      Description: Checks whether GuardDuty is enabled. You can optionally verify
        that the results are centralized in a specific AWS Account.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: GUARDDUTY_ENABLED_CENTRALIZED
    Type: AWS::Config::ConfigRule
  GuarddutyNonArchivedFindings:
    Controls:
    - DE.AE-4
    - RS.AN-2
    Properties:
      ConfigRuleName: guardduty-non-archived-findings
      Description: Checks whether Amazon GuardDuty has findings that are non archived.
        The rule is NON_COMPLIANT if Amazon GuardDuty has non archived low/medium/high
        severity findings older than the specified number in the daysLowSev/daysMediumSev/daysHighSev
        parameter.
      InputParameters:
        daysHighSev:
          Fn::If:
          - guarddutyNonArchivedFindingsParamDaysHighSev
          - Ref: GuarddutyNonArchivedFindingsParamDaysHighSev
          - Ref: AWS::NoValue
        daysLowSev:
          Fn::If:
          - guarddutyNonArchivedFindingsParamDaysLowSev
          - Ref: GuarddutyNonArchivedFindingsParamDaysLowSev
          - Ref: AWS::NoValue
        daysMediumSev:
          Fn::If:
          - guarddutyNonArchivedFindingsParamDaysMediumSev
          - Ref: GuarddutyNonArchivedFindingsParamDaysMediumSev
          - Ref: AWS::NoValue
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: GUARDDUTY_NON_ARCHIVED_FINDINGS
    Type: AWS::Config::ConfigRule
  IamGroupHasUsersCheck:
    Controls:
    - PR.AC-1
    - PR.AC-4
    Properties:
      ConfigRuleName: iam-group-has-users-check
      Description: Checks whether IAM groups have at least one IAM user.
      Scope:
        ComplianceResourceTypes:
        - AWS::IAM::Group
      Source:
        Owner: AWS
        SourceIdentifier: IAM_GROUP_HAS_USERS_CHECK
    Type: AWS::Config::ConfigRule
  IamPasswordPolicy:
    Controls:
    - PR.AC-1
    Properties:
      ConfigRuleName: iam-password-policy
      Description: Checks whether the account password policy for IAM users meets
        the specified requirements.
      InputParameters:
        MaxPasswordAge:
          Fn::If:
          - iamPasswordPolicyParamMaxPasswordAge
          - Ref: IamPasswordPolicyParamMaxPasswordAge
          - Ref: AWS::NoValue
        MinimumPasswordLength:
          Fn::If:
          - iamPasswordPolicyParamMinimumPasswordLength
          - Ref: IamPasswordPolicyParamMinimumPasswordLength
          - Ref: AWS::NoValue
        PasswordReusePrevention:
          Fn::If:
          - iamPasswordPolicyParamPasswordReusePrevention
          - Ref: IamPasswordPolicyParamPasswordReusePrevention
          - Ref: AWS::NoValue
        RequireLowercaseCharacters:
          Fn::If:
          - iamPasswordPolicyParamRequireLowercaseCharacters
          - Ref: IamPasswordPolicyParamRequireLowercaseCharacters
          - Ref: AWS::NoValue
        RequireNumbers:
          Fn::If:
          - iamPasswordPolicyParamRequireNumbers
          - Ref: IamPasswordPolicyParamRequireNumbers
          - Ref: AWS::NoValue
        RequireSymbols:
          Fn::If:
          - iamPasswordPolicyParamRequireSymbols
          - Ref: IamPasswordPolicyParamRequireSymbols
          - Ref: AWS::NoValue
        RequireUppercaseCharacters:
          Fn::If:
          - iamPasswordPolicyParamRequireUppercaseCharacters
          - Ref: IamPasswordPolicyParamRequireUppercaseCharacters
          - Ref: AWS::NoValue
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: IAM_PASSWORD_POLICY
    Type: AWS::Config::ConfigRule
  IamPolicyNoStatementsWithAdminAccess:
    Controls:
    - PR.AC-1
    - PR.AC-4
    - PR.PT-3
    Properties:
      ConfigRuleName: iam-policy-no-statements-with-admin-access
      Description: 'Checks whether the default version of AWS Identity and Access
        Management (IAM) policies do not have administrator access. If any statement
        has "Effect": "Allow" with "Action": "*" over "Resource": "*", the rule is
        non-compliant.'
      Scope:
        ComplianceResourceTypes:
        - AWS::IAM::Policy
      Source:
        Owner: AWS
        SourceIdentifier: IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS
    Type: AWS::Config::ConfigRule
  IamRootAccessKeyCheck:
    Controls:
    - PR.AC-1
    - PR.AC-4
    - PR.PT-3
    Properties:
      ConfigRuleName: iam-root-access-key-check
      Description: Checks whether the root user access key is available. The rule
        is compliant if the user access key does not exist.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: IAM_ROOT_ACCESS_KEY_CHECK
    Type: AWS::Config::ConfigRule
  IamUserGroupMembershipCheck:
    Controls:
    - ID.AM-6
    - PR.AC-1
    - PR.AC-4
    Properties:
      ConfigRuleName: iam-user-group-membership-check
      Description: Checks whether IAM users are members of at least one IAM group.
      Scope:
        ComplianceResourceTypes:
        - AWS::IAM::User
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_GROUP_MEMBERSHIP_CHECK
    Type: AWS::Config::ConfigRule
  IamUserMfaEnabled:
    Controls:
    - PR.AC-3
    - PR.AC-7
    Properties:
      ConfigRuleName: iam-user-mfa-enabled
      Description: Checks whether the AWS Identity and Access Management users have
        multi-factor authentication (MFA) enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  IamUserNoPoliciesCheck:
    Controls:
    - PR.AC-1
    - PR.AC-4
    - PR.PT-3
    Properties:
      ConfigRuleName: iam-user-no-policies-check
      Description: Checks that none of your IAM users have policies attached. IAM
        users must inherit permissions from IAM groups or roles.
      Scope:
        ComplianceResourceTypes:
        - AWS::IAM::User
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_NO_POLICIES_CHECK
    Type: AWS::Config::ConfigRule
  IamUserUnusedCredentialsCheck:
    Controls:
    - PR.AC-1
    - PR.AC-4
    Properties:
      ConfigRuleName: iam-user-unused-credentials-check
      Description: Checks whether your AWS Identity and Access Management (IAM) users
        have passwords or active access keys that have not been used within the specified
        number of days you provided.
      InputParameters:
        maxCredentialUsageAge:
          Fn::If:
          - iamUserUnusedCredentialsCheckParamMaxCredentialUsageAge
          - Ref: IamUserUnusedCredentialsCheckParamMaxCredentialUsageAge
          - Ref: AWS::NoValue
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_UNUSED_CREDENTIALS_CHECK
    Type: AWS::Config::ConfigRule
  IncomingSshDisabled:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    - DE.AE-1
    Properties:
      ConfigRuleName: restricted-ssh
      Description: Checks whether security groups that are in use disallow unrestricted
        incoming SSH traffic.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::SecurityGroup
      Source:
        Owner: AWS
        SourceIdentifier: INCOMING_SSH_DISABLED
    Type: AWS::Config::ConfigRule
  InstancesInVpc:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    Properties:
      ConfigRuleName: ec2-instances-in-vpc
      Description: Checks whether your EC2 instances belong to a virtual private cloud
        (VPC).
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::Instance
      Source:
        Owner: AWS
        SourceIdentifier: INSTANCES_IN_VPC
    Type: AWS::Config::ConfigRule
  InternetGatewayAuthorizedVpcOnly:
    Controls:
    - PR.AC-3
    Properties:
      ConfigRuleName: internet-gateway-authorized-vpc-only
      Description: Checks that Internet gateways (IGWs) are only attached to an authorized
        Amazon Virtual Private Cloud (VPCs). The rule is NON_COMPLIANT if IGWs are
        not attached to an authorized VPC.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::InternetGateway
      Source:
        Owner: AWS
        SourceIdentifier: INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY
    Type: AWS::Config::ConfigRule
  KmsCmkNotScheduledForDeletion:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: kms-cmk-not-scheduled-for-deletion
      Description: Checks whether customer master keys (CMKs) are not scheduled for
        deletion in AWS Key Management Service (KMS). The rule is NON_COMPLAINT if
        CMKs are scheduled for deletion.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes:
        - AWS::KMS::Key
      Source:
        Owner: AWS
        SourceIdentifier: KMS_CMK_NOT_SCHEDULED_FOR_DELETION
    Type: AWS::Config::ConfigRule
  LambdaConcurrencyCheck:
    Controls:
    - DE.AE-1
    Properties:
      ConfigRuleName: lambda-concurrency-check
      Description: Checks whether the AWS Lambda function is configured with function-level
        concurrent execution limit. The rule is NON_COMPLIANT if the Lambda function
        is not configured with function-level concurrent execution limit.
      Scope:
        ComplianceResourceTypes:
        - AWS::Lambda::Function
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_CONCURRENCY_CHECK
    Type: AWS::Config::ConfigRule
  LambdaDlqCheck:
    Controls:
    - DE.AE-5
    Properties:
      ConfigRuleName: lambda-dlq-check
      Description: Checks whether an AWS Lambda function is configured with a dead-letter
        queue. The rule is NON_COMPLIANT if the Lambda function is not configured
        with a dead-letter queue.
      Scope:
        ComplianceResourceTypes:
        - AWS::Lambda::Function
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_DLQ_CHECK
    Type: AWS::Config::ConfigRule
  LambdaFunctionPublicAccessProhibited:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: lambda-function-public-access-prohibited
      Description: Checks whether the Lambda function policy prohibits public access.
      Scope:
        ComplianceResourceTypes:
        - AWS::Lambda::Function
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED
    Type: AWS::Config::ConfigRule
  LambdaInsideVpc:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    Properties:
      ConfigRuleName: lambda-inside-vpc
      Description: Checks whether an AWS Lambda function is in an Amazon Virtual Private
        Cloud. The rule is NON_COMPLIANT if the Lambda function is not in a VPC.
      Scope:
        ComplianceResourceTypes:
        - AWS::Lambda::Function
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_INSIDE_VPC
    Type: AWS::Config::ConfigRule
  MfaEnabledForIamConsoleAccess:
    Controls:
    - PR.AC-3
    - PR.AC-7
    Properties:
      ConfigRuleName: mfa-enabled-for-iam-console-access
      Description: Checks whether AWS Multi-Factor Authentication (MFA) is enabled
        for all AWS Identity and Access Management (IAM) users that use a console
        password. The rule is compliant if MFA is enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS
    Type: AWS::Config::ConfigRule
  MultiRegionCloudTrailEnabled:
    Controls:
    - ID.AM-3
    - PR.AC-6
    - PR.DS-5
    - PR.MA-2
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-6
    - DE.CM-7
    Properties:
      ConfigRuleName: multi-region-cloudtrail-enabled
      Description: Checks that there is at least one multi-region AWS CloudTrail.
        The rule is non-compliant if the trails do not match input parameters
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: MULTI_REGION_CLOUD_TRAIL_ENABLED
    Type: AWS::Config::ConfigRule
  RdsEnhancedMonitoringEnabled:
    Controls:
    - PR.DS-4
    Properties:
      ConfigRuleName: rds-enhanced-monitoring-enabled
      Description: Checks whether enhanced monitoring is enabled for Amazon Relational
        Database Service (Amazon RDS) instances.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBInstance
      Source:
        Owner: AWS
        SourceIdentifier: RDS_ENHANCED_MONITORING_ENABLED
    Type: AWS::Config::ConfigRule
  RdsInstancePublicAccessCheck:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-4
    Properties:
      ConfigRuleName: rds-instance-public-access-check
      Description: Checks whether the Amazon Relational Database Service (RDS) instances
        are not publicly accessible. The rule is non-compliant if the publiclyAccessible
        field is true in the instance configuration item.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBInstance
      Source:
        Owner: AWS
        SourceIdentifier: RDS_INSTANCE_PUBLIC_ACCESS_CHECK
    Type: AWS::Config::ConfigRule
  RdsMultiAzSupport:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.PT-5
    Properties:
      ConfigRuleName: rds-multi-az-support
      Description: Checks whether high availability is enabled for your RDS DB instances.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBInstance
      Source:
        Owner: AWS
        SourceIdentifier: RDS_MULTI_AZ_SUPPORT
    Type: AWS::Config::ConfigRule
  RdsSnapshotsPublicProhibited:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: rds-snapshots-public-prohibited
      Description: Checks if Amazon Relational Database Service (Amazon RDS) snapshots
        are public. The rule is non-compliant if any existing and new Amazon RDS snapshots
        are public.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBSnapshot
        - AWS::RDS::DBClusterSnapshot
      Source:
        Owner: AWS
        SourceIdentifier: RDS_SNAPSHOTS_PUBLIC_PROHIBITED
    Type: AWS::Config::ConfigRule
  RdsStorageEncrypted:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: rds-storage-encrypted
      Description: Checks whether storage encryption is enabled for your RDS DB instances.
      Scope:
        ComplianceResourceTypes:
        - AWS::RDS::DBInstance
      Source:
        Owner: AWS
        SourceIdentifier: RDS_STORAGE_ENCRYPTED
    Type: AWS::Config::ConfigRule
  RedshiftClusterConfigurationCheck:
    Controls:
    - ID.AM-3
    - PR.AC-6
    - DE.AE-1
    - DE.AE-3
    Properties:
      ConfigRuleName: redshift-cluster-configuration-check
      Description: Checks whether Amazon Redshift clusters have the specified settings.
      InputParameters:
        clusterDbEncrypted: 'TRUE'
        loggingEnabled: 'TRUE'
      Scope:
        ComplianceResourceTypes:
        - AWS::Redshift::Cluster
      Source:
        Owner: AWS
        SourceIdentifier: REDSHIFT_CLUSTER_CONFIGURATION_CHECK
    Type: AWS::Config::ConfigRule
  RedshiftClusterPublicAccessCheck:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    - PR.PT-4
    Properties:
      ConfigRuleName: redshift-cluster-public-access-check
      Description: Checks whether Amazon Redshift clusters are not publicly accessible.
        The rule is NON_COMPLIANT if the publiclyAccessible field is true in the cluster
        configuration item.
      Scope:
        ComplianceResourceTypes:
        - AWS::Redshift::Cluster
      Source:
        Owner: AWS
        SourceIdentifier: REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK
    Type: AWS::Config::ConfigRule
  RedshiftRequireTlsSsl:
    Controls:
    - PR.DS-2
    Properties:
      ConfigRuleName: redshift-require-tls-ssl
      Description: Checks whether Amazon Redshift clusters require TLS/SSL encryption
        to connect to SQL clients. The rule is NON_COMPLIANT if any Amazon Redshift
        cluster has parameter require_SSL not set to true.
      Scope:
        ComplianceResourceTypes:
        - AWS::Redshift::Cluster
      Source:
        Owner: AWS
        SourceIdentifier: REDSHIFT_REQUIRE_TLS_SSL
    Type: AWS::Config::ConfigRule
  RestrictedIncomingTraffic:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    - DE.AE-1
    Properties:
      ConfigRuleName: restricted-common-ports
      Description: Checks whether security groups that are in use disallow unrestricted
        incoming TCP traffic to the specified ports.
      InputParameters:
        blockedPort1:
          Fn::If:
          - restrictedIncomingTrafficParamBlockedPort1
          - Ref: RestrictedIncomingTrafficParamBlockedPort1
          - Ref: AWS::NoValue
        blockedPort2:
          Fn::If:
          - restrictedIncomingTrafficParamBlockedPort2
          - Ref: RestrictedIncomingTrafficParamBlockedPort2
          - Ref: AWS::NoValue
        blockedPort3:
          Fn::If:
          - restrictedIncomingTrafficParamBlockedPort3
          - Ref: RestrictedIncomingTrafficParamBlockedPort3
          - Ref: AWS::NoValue
        blockedPort4:
          Fn::If:
          - restrictedIncomingTrafficParamBlockedPort4
          - Ref: RestrictedIncomingTrafficParamBlockedPort4
          - Ref: AWS::NoValue
        blockedPort5:
          Fn::If:
          - restrictedIncomingTrafficParamBlockedPort5
          - Ref: RestrictedIncomingTrafficParamBlockedPort5
          - Ref: AWS::NoValue
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::SecurityGroup
      Source:
        Owner: AWS
        SourceIdentifier: RESTRICTED_INCOMING_TRAFFIC
    Type: AWS::Config::ConfigRule
  RootAccountHardwareMfaEnabled:
    Controls:
    - PR.AC-3
    - PR.AC-7
    Properties:
      ConfigRuleName: root-account-hardware-mfa-enabled
      Description: Checks whether your AWS account is enabled to use multi-factor
        authentication (MFA) hardware device to sign in with root credentials.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_HARDWARE_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  RootAccountMfaEnabled:
    Controls:
    - PR.AC-3
    - PR.AC-7
    Properties:
      ConfigRuleName: root-account-mfa-enabled
      Description: Checks whether the root user of your AWS account requires multi-factor
        authentication for console sign-in.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  S3AccountLevelPublicAccessBlocks:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: s3-account-level-public-access-blocks
      Description: Checks whether the required public access block settings are configured
        from account level. The rule is NON_COMPLIANT when the public access block
        settings are not configured from account level.
      InputParameters:
        BlockPublicAcls:
          Fn::If:
          - s3AccountLevelPublicAccessBlocksParamBlockPublicAcls
          - Ref: S3AccountLevelPublicAccessBlocksParamBlockPublicAcls
          - Ref: AWS::NoValue
        BlockPublicPolicy:
          Fn::If:
          - s3AccountLevelPublicAccessBlocksParamBlockPublicPolicy
          - Ref: S3AccountLevelPublicAccessBlocksParamBlockPublicPolicy
          - Ref: AWS::NoValue
        IgnorePublicAcls:
          Fn::If:
          - s3AccountLevelPublicAccessBlocksParamIgnorePublicAcls
          - Ref: S3AccountLevelPublicAccessBlocksParamIgnorePublicAcls
          - Ref: AWS::NoValue
        RestrictPublicBuckets:
          Fn::If:
          - s3AccountLevelPublicAccessBlocksParamRestrictPublicBuckets
          - Ref: S3AccountLevelPublicAccessBlocksParamRestrictPublicBuckets
          - Ref: AWS::NoValue
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::AccountPublicAccessBlock
      Source:
        Owner: AWS
        SourceIdentifier: S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS
    Type: AWS::Config::ConfigRule
  S3BucketDefaultLockEnabled:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: s3-bucket-default-lock-enabled
      Description: Checks whether Amazon S3 bucket has lock enabled, by default. The
        rule is NON_COMPLIANT if the lock is not enabled.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_DEFAULT_LOCK_ENABLED
    Type: AWS::Config::ConfigRule
  S3BucketLoggingEnabled:
    Controls:
    - ID.AM-3
    - PR.AC-6
    - PR.DS-5
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-6
    - DE.CM-7
    Properties:
      ConfigRuleName: s3-bucket-logging-enabled
      Description: Checks whether logging is enabled for your S3 buckets.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_LOGGING_ENABLED
    Type: AWS::Config::ConfigRule
  S3BucketPolicyGranteeCheck:
    Controls:
    - PR.AC-1
    - PR.AC-3
    - PR.AC-4
    Properties:
      ConfigRuleName: s3-bucket-policy-grantee-check
      Description: Checks that the access granted by the Amazon S3 bucket is restricted
        to any of the AWS principals, federated users, service principals, IP addresses,
        or VPCs that you provide. The rule is COMPLIANT if a bucket policy is not
        present.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_POLICY_GRANTEE_CHECK
    Type: AWS::Config::ConfigRule
  S3BucketPublicReadProhibited:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: s3-bucket-public-read-prohibited
      Description: Checks that your Amazon S3 buckets do not allow public read access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
    Type: AWS::Config::ConfigRule
  S3BucketPublicWriteProhibited:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    - PR.PT-3
    Properties:
      ConfigRuleName: s3-bucket-public-write-prohibited
      Description: Checks that your Amazon S3 buckets do not allow public write access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
    Type: AWS::Config::ConfigRule
  S3BucketReplicationEnabled:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.IP-4
    - PR.PT-5
    Properties:
      ConfigRuleName: s3-bucket-replication-enabled
      Description: Checks whether the Amazon S3 buckets have cross-region replication
        enabled.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_REPLICATION_ENABLED
    Type: AWS::Config::ConfigRule
  S3BucketServerSideEncryptionEnabled:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: s3-bucket-server-side-encryption-enabled
      Description: Checks that your Amazon S3 bucket either has S3 default encryption
        enabled or that the S3 bucket policy explicitly denies put-object requests
        without server side encryption.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED
    Type: AWS::Config::ConfigRule
  S3BucketSslRequestsOnly:
    Controls:
    - PR.DS-2
    Properties:
      ConfigRuleName: s3-bucket-ssl-requests-only
      Description: Checks whether S3 buckets have policies that require requests to
        use Secure Socket Layer (SSL).
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SSL_REQUESTS_ONLY
    Type: AWS::Config::ConfigRule
  S3BucketVersioningEnabled:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.IP-4
    - PR.PT-5
    Properties:
      ConfigRuleName: s3-bucket-versioning-enabled
      Description: Checks whether versioning is enabled for your S3 buckets.
      Scope:
        ComplianceResourceTypes:
        - AWS::S3::Bucket
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_VERSIONING_ENABLED
    Type: AWS::Config::ConfigRule
  SagemakerEndpointConfigurationKmsKeyConfigured:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: sagemaker-endpoint-configuration-kms-key-configured
      Description: Checks whether AWS Key Management Service (KMS) key is configured
        for an Amazon SageMaker endpoint configuration. The rule is NON_COMPLIANT
        if 'KmsKeyId' is not specified for the Amazon SageMaker endpoint configuration.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED
    Type: AWS::Config::ConfigRule
  SagemakerNotebookInstanceKmsKeyConfigured:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: sagemaker-notebook-instance-kms-key-configured
      Description: Check whether an AWS Key Management Service (KMS) key is configured
        for an Amazon SageMaker notebook instance. The rule is NON_COMPLIANT if 'KmsKeyId'
        is not specified for the Amazon SageMaker notebook instance.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED
    Type: AWS::Config::ConfigRule
  SagemakerNotebookNoDirectInternetAccess:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.DS-5
    Properties:
      ConfigRuleName: sagemaker-notebook-no-direct-internet-access
      Description: Checks whether direct internet access is disabled for an Amazon
        SageMaker notebook instance. The rule is NON_COMPLIANT if Amazon SageMaker
        notebook instances are internet-enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS
    Type: AWS::Config::ConfigRule
  SecretsmanagerRotationEnabledCheck:
    Controls:
    - PR.AC-1
    Properties:
      ConfigRuleName: secretsmanager-rotation-enabled-check
      Description: Checks whether AWS Secret Manager secret has rotation enabled.
        If the maximumAllowedRotationFrequency parameter is specified, the rotation
        frequency of the secret is compared with the maximum allowed frequency.
      Scope:
        ComplianceResourceTypes:
        - AWS::SecretsManager::Secret
      Source:
        Owner: AWS
        SourceIdentifier: SECRETSMANAGER_ROTATION_ENABLED_CHECK
    Type: AWS::Config::ConfigRule
  SecretsmanagerScheduledRotationSuccessCheck:
    Controls:
    - PR.AC-1
    Properties:
      ConfigRuleName: secretsmanager-scheduled-rotation-success-check
      Description: Checks and verifies whether AWS Secret Manager secret rotation
        has rotated successfully as per the rotation schedule.
      Scope:
        ComplianceResourceTypes:
        - AWS::SecretsManager::Secret
      Source:
        Owner: AWS
        SourceIdentifier: SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK
    Type: AWS::Config::ConfigRule
  SecurityhubEnabled:
    Controls:
    - ID.RA-1
    - ID.RA-2
    - ID.RA-3
    - PR.DS-5
    - DE.AE-2
    - DE.AE-4
    - DE.CM-1
    - DE.CM-3
    - DE.CM-4
    - DE.CM-6
    - DE.CM-7
    Properties:
      ConfigRuleName: securityhub-enabled
      Description: Checks that AWS Security Hub is enabled for an AWS Account. The
        rule is NON_COMPLIANT if AWS Security Hub is not enabled.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: SECURITYHUB_ENABLED
    Type: AWS::Config::ConfigRule
  ShieldDrtAccess:
    Controls:
    - DE.AE-2
    - DE.AE-4
    - DE.CM-1
    Properties:
      ConfigRuleName: shield-drt-access
      Description: Verify that DDoS response team (DRT) can access AWS account. The
        rule is NON_COMPLIANT if AWS Shield Advanced is enabled but the role for DRT
        access is not configured.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: SHIELD_DRT_ACCESS
    Type: AWS::Config::ConfigRule
  SnsEncryptedKms:
    Controls:
    - PR.DS-1
    Properties:
      ConfigRuleName: sns-encrypted-kms
      Description: Checks whether Amazon SNS topic is encrypted with AWS Key Management
        Service (AWS KMS). The rule is NON_COMPLIANT if the Amazon SNS topic is not
        encrypted with AWS KMS.
      Scope:
        ComplianceResourceTypes:
        - AWS::SNS::Topic
      Source:
        Owner: AWS
        SourceIdentifier: SNS_ENCRYPTED_KMS
    Type: AWS::Config::ConfigRule
  VpcDefaultSecurityGroupClosed:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - DE.AE-1
    Properties:
      ConfigRuleName: vpc-default-security-group-closed
      Description: Checks that the default security group of any Amazon Virtual Private
        Cloud (VPC) does not allow inbound or outbound traffic. The rule is non-compliant
        if the default security group has one or more inbound or outbound traffic.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::SecurityGroup
      Source:
        Owner: AWS
        SourceIdentifier: VPC_DEFAULT_SECURITY_GROUP_CLOSED
    Type: AWS::Config::ConfigRule
  VpcFlowLogsEnabled:
    Controls:
    - ID.AM-3
    - PR.DS-5
    - PR.PT-1
    - DE.AE-1
    - DE.AE-3
    - DE.CM-1
    - DE.CM-7
    Properties:
      ConfigRuleName: vpc-flow-logs-enabled
      Description: Checks whether Amazon Virtual Private Cloud flow logs are found
        and enabled for Amazon VPC.
      MaximumExecutionFrequency: TwentyFour_Hours
      Scope: {}
      Source:
        Owner: AWS
        SourceIdentifier: VPC_FLOW_LOGS_ENABLED
    Type: AWS::Config::ConfigRule
  VpcSgOpenOnlyToAuthorizedPorts:
    Controls:
    - PR.AC-3
    - PR.AC-5
    - PR.PT-4
    - DE.AE-1
    Properties:
      ConfigRuleName: vpc-sg-open-only-to-authorized-ports
      Description: Checks whether any security groups with inbound 0.0.0.0/0 have
        TCP or UDP ports accessible. The rule is NON_COMPLIANT when a security group
        with inbound 0.0.0.0/0 has a port accessible which is not specified in the
        rule parameters.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::SecurityGroup
      Source:
        Owner: AWS
        SourceIdentifier: VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS
    Type: AWS::Config::ConfigRule
  VpcVpn2TunnelsUp:
    Controls:
    - ID.BE-5
    - PR.DS-4
    - PR.PT-5
    Properties:
      ConfigRuleName: vpc-vpn-2-tunnels-up
      Description: Checks that both VPN tunnels provided by AWS Site-to-Site VPN are
        in UP status. The rule returns NON_COMPLIANT if one or both tunnels are in
        DOWN status.
      Scope:
        ComplianceResourceTypes:
        - AWS::EC2::VPNConnection
      Source:
        Owner: AWS
        SourceIdentifier: VPC_VPN_2_TUNNELS_UP
    Type: AWS::Config::ConfigRule
```