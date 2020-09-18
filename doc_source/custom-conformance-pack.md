# Custom Conformance Pack<a name="custom-conformance-pack"></a>

```
#######################################################################################################
#
#   Conformance Pack:
#     Example Conformance Pack with a custom AWS Config Rule
#
#   Example conformance pack template with a custom AWS Config rule along with other managed rules.
# 
#######################################################################################################
       
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