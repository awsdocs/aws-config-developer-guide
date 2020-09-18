# Example Templates with Remediation Action<a name="templateswithremediation"></a>

## Operational Best Practices For Amazon DynamoDB with Remediation<a name="operational-best-practices-for-amazon-dynamodb-with-remediation"></a>

```
################################################################################
#
#   Conformance Pack:
#     Operational Best Practices for Amazon DynamoDB, with Remediation
#
#   See Parameters section for names and descriptions of required parameters.
#
################################################################################

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

## Operational Best Practices For Amazon S3 with Remediation<a name="operational-best-practices-for-amazon-s3-with-remediation"></a>

```
################################################################################
#
#   Conformance Pack:
#     Operational Best Practices for Amazon S3 with Remediation
#
#   See Parameters section for names and descriptions of required parameters.
#
################################################################################

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