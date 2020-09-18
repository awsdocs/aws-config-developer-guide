# Operational Best Practices For Amazon DynamoDB<a name="operational-best-practices-for-amazon-dynamodb"></a>

```
####################################################################################################
#
#   Conformance Pack:
#     Operational Best Practices for Amazon DynamoDB
#
#   This pack contains AWS Config rules based on the best practice guidelines for Amazon DynamoDB.
#
####################################################################################################

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