# Conformance Pack Sample Templates<a name="conformancepack-sample-templates"></a>

In the conformance pack template, you can use one or more AWS Config rules and remediation actions\. The AWS Config rules and custom rules can be managed\.

**Topics**
+ [Operational Best Practices For Amazon S3](#operational-best-practices-for-amazon-s3)
+ [Operational Best Practices For Amazon DynamoDB](#operational-best-practices-for-amazon-dynamodb)
+ [Operational Best Practices For PCI\-DSS](#operational-best-practices-for-pci-dss)
+ [Operational Best Practices For AWS Identity And Access Management](#operational-best-practices-for-aws-identity-and-access-management)
+ [Templates With Remediation](#templateswithremediation)
+ [Custom Conformance Pack](#custom-conformance-pack)

Few conformance pack YAML templates that you see in AWS Config console are as follows\.

## Operational Best Practices For Amazon S3<a name="operational-best-practices-for-amazon-s3"></a>

```
Resources:
  S3BucketPublicReadProhibited:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited
      Description: >- 
        Checks that your Amazon S3 buckets do not allow public read access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
      MaximumExecutionFrequency: Six_Hours
  S3BucketPublicWriteProhibited: 
    Type: "AWS::Config::ConfigRule"
    Properties: 
      ConfigRuleName: S3BucketPublicWriteProhibited
      Description: "Checks that your Amazon S3 buckets do not allow public write access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL)."
      Scope: 
        ComplianceResourceTypes: 
        - "AWS::S3::Bucket"
      Source: 
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
      MaximumExecutionFrequency: Six_Hours
  S3BucketReplicationEnabled: 
    Type: "AWS::Config::ConfigRule"
    Properties: 
      ConfigRuleName: S3BucketReplicationEnabled
      Description: "Checks whether the Amazon S3 buckets have cross-region replication enabled."
      Scope: 
        ComplianceResourceTypes: 
        - "AWS::S3::Bucket"
      Source: 
        Owner: AWS
        SourceIdentifier: S3_BUCKET_REPLICATION_ENABLED
  S3BucketSSLRequestsOnly: 
    Type: "AWS::Config::ConfigRule"
    Properties: 
      ConfigRuleName: S3BucketSSLRequestsOnly
      Description: "Checks whether S3 buckets have policies that require requests to use Secure Socket Layer (SSL)."
      Scope: 
        ComplianceResourceTypes: 
        - "AWS::S3::Bucket"
      Source: 
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SSL_REQUESTS_ONLY
  ServerSideReplicationEnabled: 
    Type: "AWS::Config::ConfigRule"
    Properties: 
      ConfigRuleName: ServerSideReplicationEnabled
      Description: "Checks that your Amazon S3 bucket either has S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption."
      Scope: 
        ComplianceResourceTypes: 
        - "AWS::S3::Bucket"
      Source: 
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED
  S3BucketLoggingEnabled: 
    Type: "AWS::Config::ConfigRule"
    Properties: 
      ConfigRuleName: S3BucketLoggingEnabled
      Description: "Checks whether logging is enabled for your S3 buckets."
      Scope: 
        ComplianceResourceTypes: 
        - "AWS::S3::Bucket"
      Source: 
        Owner: AWS
        SourceIdentifier: S3_BUCKET_LOGGING_ENABLED
```

## Operational Best Practices For Amazon DynamoDB<a name="operational-best-practices-for-amazon-dynamodb"></a>

```
---
Resources:
  DynamoDbAutoscalingEnabled:
    Properties:
      ConfigRuleName: DynamoDbAutoscalingEnabled
      Description: "This rule checks whether Auto Scaling is enabled on your DynamoDB tables. Optionally you can set the read and write capacity units for the table."
      MaximumExecutionFrequency: Six_Hours
      Scope:
        ComplianceResourceTypes:
          - "AWS::DynamoDB::Table"
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_AUTOSCALING_ENABLED
    Type: "AWS::Config::ConfigRule"
  DynamoDbTableEncryptionEnabled:
    Properties:
      ConfigRuleName: DynamoDbTableEncryptionEnabled
      Description: "Checks whether the Amazon DynamoDB tables are encrypted and checks their status. The rule is compliant if the status is enabled or enabling."
      Scope:
        ComplianceResourceTypes:
          - "AWS::DynamoDB::Table"
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_TABLE_ENCRYPTION_ENABLED
    Type: "AWS::Config::ConfigRule"
  DynamoDbThroughputLimitCheck:
    Properties:
      ConfigRuleName: DynamoDbThroughputLimitCheck
      Description: "Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account."
      MaximumExecutionFrequency: Six_Hours
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_THROUGHPUT_LIMIT_CHECK
    Type: "AWS::Config::ConfigRule"
```

## Operational Best Practices For PCI\-DSS<a name="operational-best-practices-for-pci-dss"></a>

This template accepts parameters\. 

```
Parameters:
  S3BucketBlacklistedActionsProhibitedParameterBlacklistedActionPattern:
    Description: Comma-separated list of blacklisted action patterns, for example,
      s3:GetBucket* and s3:DeleteObject.
    Type: String
  S3BucketPolicyNotMorePermissiveParameterControlPolicy:
    Description: Amazon S3 bucket policy that defines an upper bound on the permissions
      of your S3 buckets. The policy can be a maximum of 1024 characters long.
    Type: String
Resources:
  DMSReplicationNotPublic:
    Properties:
      ConfigRuleName: DMSReplicationNotPublic
      Description: Checks whether AWS Database Migration Service replication instances
        are public. The rule is NON_COMPLIANT if PubliclyAccessible field is True.
      Source:
        Owner: AWS
        SourceIdentifier: DMS_REPLICATION_NOT_PUBLIC
    Type: AWS::Config::ConfigRule
  EBSSnapshotPublicRestorableCheck:
    Properties:
      ConfigRuleName: EBSSnapshotPublicRestorableCheck
      Description: Checks whether Amazon Elastic Block Store (Amazon EBS) snapshots
        are not publicly restorable. The rule is NON_COMPLIANT if one or more snapshots
        with RestorableByUserIds field are set to all, that is, Amazon EBS snapshots
        are public.
      Source:
        Owner: AWS
        SourceIdentifier: EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK
    Type: AWS::Config::ConfigRule
  EC2InstanceNoPublicIP:
    Properties:
      ConfigRuleName: EC2InstanceNoPublicIP
      Description: Checks whether Amazon Elastic Compute Cloud (Amazon EC2) instances
        have a public IP association. The rule is NON_COMPLIANT if the publicIp field
        is present in the Amazon EC2 instance configuration item. This rule applies
        only to IPv4.
      Source:
        Owner: AWS
        SourceIdentifier: EC2_INSTANCE_NO_PUBLIC_IP
    Type: AWS::Config::ConfigRule
  ElasticsearchInVPCOnly:
    Properties:
      ConfigRuleName: ElasticsearchInVPCOnly
      Description: Checks whether Amazon Elasticsearch Service domains are in Amazon
        Virtual Private Cloud (Amazon VPC). The rule is NON_COMPLIANT if Amazon ElasticSearch Service domain endpoint is public.
      Source:
        Owner: AWS
        SourceIdentifier: ELASTICSEARCH_IN_VPC_ONLY
    Type: AWS::Config::ConfigRule
  IAMRootAccessKeyCheck:
    Properties:
      ConfigRuleName: IAMRootAccessKeyCheck
      Description: Checks whether the root user access key is available. The rule
        is compliant if the user access key does not exist.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_ROOT_ACCESS_KEY_CHECK
    Type: AWS::Config::ConfigRule
  IAMUserMFAEnabled:
    Properties:
      ConfigRuleName: IAMUserMFAEnabled
      Description: Checks whether the AWS Identity and Access Management users have
        multi-factor authentication (MFA) enabled.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  IncomingSSHDisabled:
    Properties:
      ConfigRuleName: IncomingSSHDisabled
      Description: Checks whether security groups that are in use disallow unrestricted
        incoming SSH traffic.
      Source:
        Owner: AWS
        SourceIdentifier: INCOMING_SSH_DISABLED
    Type: AWS::Config::ConfigRule
  InstancesInVPC:
    Properties:
      ConfigRuleName: InstancesInVPC
      Description: Checks whether your EC2 instances belong to a virtual private cloud
        (VPC).
      Source:
        Owner: AWS
        SourceIdentifier: INSTANCES_IN_VPC
    Type: AWS::Config::ConfigRule
  LambdaFunctionPublicAccessProhibited:
    Properties:
      ConfigRuleName: LambdaFunctionPublicAccessProhibited
      Description: Checks whether the Lambda function policy prohibits public access.
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED
    Type: AWS::Config::ConfigRule
  LambdaInsideVPC:
    Properties:
      ConfigRuleName: LambdaInsideVPC
      Description: Checks whether an AWS Lambda function is in an Amazon Virtual Private
        Cloud. The rule is NON_COMPLIANT if the Lambda function is not in a VPC.
      Source:
        Owner: AWS
        SourceIdentifier: LAMBDA_INSIDE_VPC
    Type: AWS::Config::ConfigRule
  MFAEnabledForIAMConsoleAccess:
    Properties:
      ConfigRuleName: MFAEnabledForIAMConsoleAccess
      Description: Checks whether AWS Multi-Factor Authentication (MFA) is enabled
        for all AWS Identity and Access Management (IAM) users that use a console
        password. The rule is compliant if MFA is enabled.
      Source:
        Owner: AWS
        SourceIdentifier: MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS
    Type: AWS::Config::ConfigRule
  RDSInstancePublicAccessCheck:
    Properties:
      ConfigRuleName: RDSInstancePublicAccessCheck
      Description: Checks whether the Amazon Relational Database Service (Amazon RDS) instances
        are not publicly accessible. The rule is non-compliant if the publiclyAccessible
        field is true in the instance configuration item.
      Source:
        Owner: AWS
        SourceIdentifier: RDS_INSTANCE_PUBLIC_ACCESS_CHECK
    Type: AWS::Config::ConfigRule
  RDSSnapshotsPublicProhibited:
    Properties:
      ConfigRuleName: RDSSnapshotsPublicProhibited
      Description: Checks if Amazon Relational Database Service (Amazon RDS) snapshots
        are public. The rule is non-compliant if any existing and new Amazon RDS snapshots
        are public.
      Source:
        Owner: AWS
        SourceIdentifier: RDS_SNAPSHOTS_PUBLIC_PROHIBITED
    Type: AWS::Config::ConfigRule
  RedshiftClusterPublicAccessCheck:
    Properties:
      ConfigRuleName: RedshiftClusterPublicAccessCheck
      Description: Checks whether Amazon Redshift clusters are not publicly accessible.
        The rule is NON_COMPLIANT if the publiclyAccessible field is true in the cluster
        configuration item.
      Source:
        Owner: AWS
        SourceIdentifier: REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK
    Type: AWS::Config::ConfigRule
  RestrictedIncomingTraffic:
    Properties:
      ConfigRuleName: RestrictedIncomingTraffic
      Description: Checks whether security groups that are in use disallow unrestricted
        incoming TCP traffic to the specified ports.
      Source:
        Owner: AWS
        SourceIdentifier: RESTRICTED_INCOMING_TRAFFIC
    Type: AWS::Config::ConfigRule
  RootAccountHardwareMFAEnabled:
    Properties:
      ConfigRuleName: RootAccountHardwareMFAEnabled
      Description: Checks whether your AWS account is enabled to use multi-factor
        authentication (MFA) hardware device to sign in with root credentials.
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_HARDWARE_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  RootAccountMFAEnabled:
    Properties:
      ConfigRuleName: RootAccountMFAEnabled
      Description: Checks whether the root user of your AWS account requires multi-factor
        authentication for console sign-in.
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  S3BucketBlacklistedActionsProhibited:
    Properties:
      ConfigRuleName: S3BucketBlacklistedActionsProhibited
      Description: Checks that the S3 bucket policy does not allow blacklisted bucket-level
        and object-level actions for principals from other AWS Accounts. The rule
        is non-compliant if any blacklisted actions are allowed by the S3 bucket policy.
      InputParameters:
        blacklistedActionPattern:
          Ref: S3BucketBlacklistedActionsProhibitedParameterBlacklistedActionPattern
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_BLACKLISTED_ACTIONS_PROHIBITED
    Type: AWS::Config::ConfigRule
  S3BucketPolicyGranteeCheck:
    Properties:
      ConfigRuleName: S3BucketPolicyGranteeCheck
      Description: Checks that the access granted by the Amazon S3 bucket is restricted
        to any of the AWS principals, federated users, service principals, IP addresses,
        or VPCs that you provide. The rule is COMPLIANT if a bucket policy is not
        present.
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_POLICY_GRANTEE_CHECK
    Type: AWS::Config::ConfigRule
  S3BucketPolicyNotMorePermissive:
    Properties:
      ConfigRuleName: S3BucketPolicyNotMorePermissive
      Description: Verifies that your Amazon S3 bucket policies do not allow other
        inter-account permissions than the control S3 bucket policy that you provide.
      InputParameters:
        controlPolicy:
          Ref: S3BucketPolicyNotMorePermissiveParameterControlPolicy
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE
    Type: AWS::Config::ConfigRule
  S3BucketPublicReadProhibited1:
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited1
      Description: Checks that your Amazon S3 buckets do not allow public read access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
    Type: AWS::Config::ConfigRule
  S3BucketPublicWriteProhibited:
    Properties:
      ConfigRuleName: S3BucketPublicWriteProhibited
      Description: Checks that your Amazon S3 buckets do not allow public write access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
    Type: AWS::Config::ConfigRule
  S3BucketVersioningEnabled:
    Properties:
      ConfigRuleName: S3BucketVersioningEnabled
      Description: Checks whether versioning is enabled for your S3 buckets.
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_VERSIONING_ENABLED
    Type: AWS::Config::ConfigRule
  VPCDefaultSecurityGroupClosed:
    Properties:
      ConfigRuleName: VPCDefaultSecurityGroupClosed
      Description: Checks that the default security group of any Amazon Virtual Private Cloud (Amazon VPC) does not allow inbound or outbound traffic. The rule is non-compliant if the default security group has inbound or outbound traffic.
      Source:
        Owner: AWS
        SourceIdentifier: VPC_DEFAULT_SECURITY_GROUP_CLOSED
    Type: AWS::Config::ConfigRule
  VPCSGOpenOnlyToAuthorizedPorts:
    Properties:
      ConfigRuleName: VPCSGOpenOnlyToAuthorizedPorts
      Description: Checks whether any security groups with inbound 0.0.0.0/0 have
        TCP or UDP ports accessible. The rule is NON_COMPLIANT when a security group
        with inbound 0.0.0.0/0 has a port accessible which is not specified in the
        rule parameters.
      Source:
        Owner: AWS
        SourceIdentifier: VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS
    Type: AWS::Config::ConfigRule
```

## Operational Best Practices For AWS Identity And Access Management<a name="operational-best-practices-for-aws-identity-and-access-management"></a>

This template accepts parameters\.

```
Parameters:
  AccessKeysRotatedParameterMaxAccessKeyAge:
    Description: Maximum number of days without rotation. Default 90.
    Type: String
  IAMPolicyBlacklistedCheckParameterPolicyArns:
    Description: Comma-separated list of IAM policy ARNs that should not be attached to any IAM entity.
    Type: String
  IAMRoleManagedPolicyCheckParameterManagedPolicyArns:
    Description: Comma-separated list of AWS managed policy ARNs.
    Type: String
  IAMUserUnusedCredentialsCheckParameterMaxCredentialUsageAge:
    Description: Maximum number of days a credential cannot be used. The default value
      is 90 days.
    Type: String
Resources:
  AccessKeysRotated:
    Properties:
      ConfigRuleName: AccessKeysRotated
      Description: Checks whether the active access keys are rotated within the number
        of days specified in maxAccessKeyAge. The rule is non-compliant if the access
        keys have not been rotated for more than maxAccessKeyAge number of days.
      InputParameters:
        maxAccessKeyAge:
          Ref: AccessKeysRotatedParameterMaxAccessKeyAge
      Source:
        Owner: AWS
        SourceIdentifier: ACCESS_KEYS_ROTATED
    Type: AWS::Config::ConfigRule
  IAMGroupHasUsersCheck:
    Properties:
      ConfigRuleName: IAMGroupHasUsersCheck
      Description: Checks whether IAM groups have at least one IAM user.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_GROUP_HAS_USERS_CHECK
    Type: AWS::Config::ConfigRule
  IAMPasswordPolicy:
    Properties:
      ConfigRuleName: IAMPasswordPolicy
      Description: Checks whether the account password policy for IAM users meets
        the specified requirements.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_PASSWORD_POLICY
    Type: AWS::Config::ConfigRule
  IAMPolicyBlacklistedCheck:
    Properties:
      ConfigRuleName: IAMPolicyBlacklistedCheck
      Description: Checks that none of your IAM users, groups, or roles (excluding
        exceptionList) have the specified policies attached.
      InputParameters:
        policyArns:
          Ref: IAMPolicyBlacklistedCheckParameterPolicyArns
      Source:
        Owner: AWS
        SourceIdentifier: IAM_POLICY_BLACKLISTED_CHECK
    Type: AWS::Config::ConfigRule
  IAMPolicyNoStatementsWithAdminAccess:
    Properties:
      ConfigRuleName: IAMPolicyNoStatementsWithAdminAccess
      Description: Checks whether the default version of AWS Identity and Access
        Management (IAM) policies do not have administrator access. If any statement
        has "Effect": "Allow" with "Action": "*" over "Resource": "*", the rule is
        non-compliant.'
      Source:
        Owner: AWS
        SourceIdentifier: IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS
    Type: AWS::Config::ConfigRule
  IAMRoleManagedPolicyCheck:
    Properties:
      ConfigRuleName: IAMRoleManagedPolicyCheck
      Description: Checks that the AWS Identity and Access Management (IAM) role is
        attached to all AWS managed policies specified in the list of managed policies.
        The rule is non-compliant if the IAM role is not attached to the AWS managed
        policy.
      InputParameters:
        managedPolicyArns:
          Ref: IAMRoleManagedPolicyCheckParameterManagedPolicyArns
      Source:
        Owner: AWS
        SourceIdentifier: IAM_ROLE_MANAGED_POLICY_CHECK
    Type: AWS::Config::ConfigRule
  IAMRootAccessKeyCheck:
    Properties:
      ConfigRuleName: IAMRootAccessKeyCheck
      Description: Checks whether the root user access key is available. The rule
        is compliant if the user access key does not exist.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_ROOT_ACCESS_KEY_CHECK
    Type: AWS::Config::ConfigRule
  IAMUserGroupMembershipCheck:
    Properties:
      ConfigRuleName: IAMUserGroupMembershipCheck
      Description: Checks whether IAM users are members of at least one IAM group.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_GROUP_MEMBERSHIP_CHECK
    Type: AWS::Config::ConfigRule
  IAMUserMFAEnabled:
    Properties:
      ConfigRuleName: IAMUserMFAEnabled
      Description: Checks whether the AWS Identity and Access Management users have
        multi-factor authentication (MFA) enabled.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  IAMUserNoPoliciesCheck:
    Properties:
      ConfigRuleName: IAMUserNoPoliciesCheck
      Description: Checks that none of your IAM users have policies attached. IAM
        users must inherit permissions from IAM groups or roles.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_NO_POLICIES_CHECK
    Type: AWS::Config::ConfigRule
  IAMUserUnusedCredentialsCheck:
    Properties:
      ConfigRuleName: IAMUserUnusedCredentialsCheck
      Description: Checks whether your AWS Identity and Access Management (IAM) users
        have passwords or active access keys that have not been used within the specified
        number of days you provided.
      InputParameters:
        maxCredentialUsageAge:
          Ref: IAMUserUnusedCredentialsCheckParameterMaxCredentialUsageAge
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_UNUSED_CREDENTIALS_CHECK
    Type: AWS::Config::ConfigRule
  MFAEnabledForIAMConsoleAccess:
    Properties:
      ConfigRuleName: MFAEnabledForIAMConsoleAccess
      Description: Checks whether AWS Multi-Factor Authentication (MFA) is enabled
        for all AWS Identity and Access Management (IAM) users that use a console
        password. The rule is compliant if MFA is enabled.
      Source:
        Owner: AWS
        SourceIdentifier: MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS
    Type: AWS::Config::ConfigRule
  RootAccountHardwareMFAEnabled:
    Properties:
      ConfigRuleName: RootAccountHardwareMFAEnabled
      Description: Checks whether your AWS account is enabled to use a multi-factor
        authentication (MFA) hardware device to sign in with root credentials.
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_HARDWARE_MFA_ENABLED
    Type: AWS::Config::ConfigRule
  RootAccountMFAEnabled:
    Properties:
      ConfigRuleName: RootAccountMFAEnabled
      Description: Checks whether the root user of your AWS account requires multi-factor
        authentication for console sign-in.
      Source:
        Owner: AWS
        SourceIdentifier: ROOT_ACCOUNT_MFA_ENABLED
    Type: AWS::Config::ConfigRule
```

## Templates With Remediation<a name="templateswithremediation"></a>

### Operational Best Practices For Amazon DynamoDB with Remediation<a name="operational-best-practices-for-amazon-dynamodb-with-remediation"></a>

```
---
Parameters:
  SnsTopicForPublishNotificationArn:
    Description: The ARN of the SNS topic to which the notification about the auto-remediation status should be published.
    Type: String

Resources:
  DynamoDbAutoscalingEnabled:
    Properties:
      ConfigRuleName: DynamoDbAutoscalingEnabled
      Description: "This rule checks whether Auto Scaling is enabled on your DynamoDB tables. Optionally you can set the read and write capacity units for the table."
      MaximumExecutionFrequency: Six_Hours
      Scope:
        ComplianceResourceTypes:
          - "AWS::DynamoDB::Table"
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_AUTOSCALING_ENABLED
    Type: "AWS::Config::ConfigRule"
  DynamoDbAutoscalingEnabledManualRemediation:
    DependsOn: DynamoDbAutoscalingEnabled
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: DynamoDbAutoscalingEnabled
      ResourceType: "AWS::DynamoDB::Table"
      TargetId: "AWS-PublishSNSNotification"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values: 
              - "arn:aws:iam::Account ID:role/PublishSnsAutomationExecutionRole"
        Message:
          StaticValue:
            Values:
              - "A table with no autoscaling configuration found"
        TopicArn:
          StaticValue:
            Values:
              - Ref: SnsTopicForPublishNotificationArn

  DynamoDbTableEncryptionEnabled:
    Properties:
      ConfigRuleName: DynamoDbTableEncryptionEnabled
      Description: "Checks whether the Amazon DynamoDB tables are encrypted and checks their status. The rule is compliant if the status is enabled or enabling."
      Scope:
        ComplianceResourceTypes:
          - "AWS::DynamoDB::Table"
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_TABLE_ENCRYPTION_ENABLED
    Type: "AWS::Config::ConfigRule"
  DynamoDbTableEncryptionEnabledAutoRemediation:
    DependsOn: DynamoDbTableEncryptionEnabled
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: DynamoDbTableEncryptionEnabled
      ResourceType: "AWS::DynamoDB::Table"
      TargetId: "AWS-PublishSNSNotification"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values: 
              - "arn:aws:iam::Account ID:role/PublishSnsAutomationExecutionRole"
        Message:
          StaticValue:
            Values:
              - "A table with no encryption enabled is found"
        TopicArn:
          StaticValue:
            Values:
              - Ref: SnsTopicForPublishNotificationArn
      ExecutionControls:
        SsmControls:
          ConcurrentExecutionRatePercentage: 10
          ErrorPercentage: 10
      Automatic: True
      MaximumAutomaticAttempts: 10
      RetryAttemptSeconds: 600

  DynamoDbThroughputLimitCheck:
    Properties:
      ConfigRuleName: DynamoDbThroughputLimitCheck
      Description: "Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account."
      MaximumExecutionFrequency: Six_Hours
      Source:
        Owner: AWS
        SourceIdentifier: DYNAMODB_THROUGHPUT_LIMIT_CHECK
    Type: "AWS::Config::ConfigRule"
```

### Operational Best Practices For Amazon S3 with Remediation<a name="operational-best-practices-for-amazon-s3-with-remediation"></a>

```
Parameters:
  S3TargetBucketNameForEnableLogging:
    Description: The target s3 bucket where the logging should be enabled.
    Type: String
Resources:
  S3BucketPublicReadProhibited:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited
      Description: >-
        Checks that your Amazon S3 buckets do not allow public read access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
      MaximumExecutionFrequency: Six_Hours
  S3PublicReadRemediation:
    DependsOn: S3BucketPublicReadProhibited
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited
      ResourceType: "AWS::S3::Bucket"
      TargetId: "AWS-DisableS3BucketPublicReadWrite"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values:
              - arn:aws:iam::Account ID:role/S3OperationsAutomationsExecutionRole
        S3BucketName:
          ResourceValue:
            Value: "RESOURCE_ID"
      ExecutionControls:
        SsmControls:
          ConcurrentExecutionRatePercentage: 10
          ErrorPercentage: 10
      Automatic: True
      MaximumAutomaticAttempts: 10
      RetryAttemptSeconds: 600

  S3BucketPublicWriteProhibited:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: S3BucketPublicWriteProhibited
      Description: "Checks that your Amazon S3 buckets do not allow public write access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL)."
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
      MaximumExecutionFrequency: Six_Hours
  S3PublicWriteRemediation:
    DependsOn: S3BucketPublicWriteProhibited
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: S3BucketPublicWriteProhibited
      ResourceType: "AWS::S3::Bucket"
      TargetId: "AWS-DisableS3BucketPublicReadWrite"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values:
              - arn:aws:iam::Account ID:role/S3OperationsAutomationsExecutionRole
        S3BucketName:
          ResourceValue:
            Value: "RESOURCE_ID"
      ExecutionControls:
        SsmControls:
          ConcurrentExecutionRatePercentage: 10
          ErrorPercentage: 10
      Automatic: True
      MaximumAutomaticAttempts: 10
      RetryAttemptSeconds: 600

  S3BucketReplicationEnabled:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: S3BucketReplicationEnabled
      Description: "Checks whether the Amazon S3 buckets have cross-region replication enabled."
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_REPLICATION_ENABLED
  S3BucketSSLRequestsOnly:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: S3BucketSSLRequestsOnly
      Description: "Checks whether S3 buckets have policies that require requests to use Secure Socket Layer (SSL)."
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SSL_REQUESTS_ONLY

  S3BucketServerSideEncryptionEnabled:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: S3BucketServerSideEncryptionEnabled
      Description: "Checks that your Amazon S3 bucket either has S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption."
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED
  S3BucketServerSideEncryptionEnabledRemediation:
    DependsOn: S3BucketServerSideEncryptionEnabled
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: S3BucketServerSideEncryptionEnabled
      ResourceType: "AWS::S3::Bucket"
      TargetId: "AWS-EnableS3BucketEncryption"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values:
              - arn:aws:iam::Account ID:role/S3OperationsAutomationsExecutionRole
        BucketName:
          ResourceValue:
            Value: "RESOURCE_ID"
        SSEAlgorithm:
          StaticValue:
            Values:
              - "AES256"
      ExecutionControls:
        SsmControls:
          ConcurrentExecutionRatePercentage: 10
          ErrorPercentage: 10
      Automatic: True
      MaximumAutomaticAttempts: 10
      RetryAttemptSeconds: 600

  S3BucketLoggingEnabled:
    Type: "AWS::Config::ConfigRule"
    Properties:
      ConfigRuleName: S3BucketLoggingEnabled
      Description: "Checks whether logging is enabled for your S3 buckets."
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_LOGGING_ENABLED
  S3BucketLoggingEnabledRemediation:
    DependsOn: S3BucketLoggingEnabled
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: S3BucketLoggingEnabled
      ResourceType: "AWS::S3::Bucket"
      TargetId: "AWS-ConfigureS3BucketLogging"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values:
              - arn:aws:iam::Account ID:role/S3OperationsAutomationsExecutionRole
        BucketName:
          ResourceValue:
            Value: "RESOURCE_ID"
        TargetBucket:
          StaticValue:
            Values:
              - Ref: S3TargetBucketNameForEnableLogging
        GrantedPermission:
          StaticValue:
            Values:
              - "FULL_CONTROL"
        GranteeType:
          StaticValue:
            Values:
              - "Group"
        GranteeUri:
          StaticValue:
            Values:
              - "http://acs.amazonaws.com/groups/s3/LogDelivery"
      ExecutionControls:
        SsmControls:
          ConcurrentExecutionRatePercentage: 10
          ErrorPercentage: 10
      Automatic: True
      MaximumAutomaticAttempts: 10
      RetryAttemptSeconds: 600
```

## Custom Conformance Pack<a name="custom-conformance-pack"></a>

```
Parameters:
  CustomConfigRuleLambdaArn:
    Description: The ARN of the custom config rule lambda.
    Type: String
Resources:
  CustomRuleForEC2:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: "CustomRuleForEC2"
      Scope:
        ComplianceResourceTypes:
          - "AWS::EC2::Volume"
      Source:
        Owner: "CUSTOM_LAMBDA"
        SourceDetails:
          -
            EventSource: "aws.config"
            MessageType: "ConfigurationItemChangeNotification"
          -
            EventSource: "aws.config"
            MessageType: "OversizedConfigurationItemChangeNotification"
        SourceIdentifier:
          Ref: CustomConfigRuleLambdaArn
  ConfigRuleForVolumeTags:
    Type: AWS::Config::ConfigRule
    Description: "Test CREATE"
    Properties:
      ConfigRuleName: "ConfigRuleForVolumeTags"
      InputParameters:
        tag1Key: CostCenter
      Scope:
        ComplianceResourceTypes:
          - "AWS::EC2::Volume"
      Source:
        Owner: AWS
        SourceIdentifier: "REQUIRED_TAGS"
  CloudTrailEnabled:
    Type: AWS::Config::ConfigRule
    Description: "CloudTrail rule"
    Properties:
      ConfigRuleName: "CloudTrailEnabled"
      InputParameters:
        s3BucketName: testBucketName
      Source:
        Owner: AWS
        SourceIdentifier: "CLOUD_TRAIL_ENABLED"
```

For more information about template structure, see [Template Anatomy](&url-cfn-user;template-anatomy.html) in AWS CloudFormation user guide\.