# Viewing Configuration Compliance<a name="evaluate-config_view-compliance"></a>

You can use the AWS Config console, AWS CLI, or AWS Config API to view the compliance state of your rules and resources\.

**To view compliance \(console\)**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. In the navigation pane, choose **Rules**\. The console shows the **Rules** page, which lists your rules and the compliance status of each\.

1. Choose a rule to view its **Rule details** page\. This page shows the rule's configuration, its status, and any AWS resources that do not comply with it\.

1. If the **Rule details** shows any noncompliant resources, choose the **Config timeline** icon \(![\[Config timeline icon.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/config-timeline.png)\) for a resource to see its configuration timeline page\. The page shows the configuration settings that AWS Config captured when it detected that the resource was noncompliant\. This information can help you determine why the resource fails to comply with the rule\. For more information, see [Viewing Configuration Details](view-manage-resource-console.md)\.

You can also view the compliance of your resources by looking them up on the **Resource inventory** page\. For more information, see [Looking Up Resources That Are Discovered by AWS Config](looking-up-discovered-resources.md)\.

**Example To view compliance \(AWS CLI\)**  
To view compliance, use any of the following CLI commands:  
+ To see the compliance state of each of your rules, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-compliance-by-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-compliance-by-config-rule.html) command, as shown in the following example:

  ```
  $ aws configservice describe-compliance-by-config-rule
  {
      "ComplianceByConfigRules": [
          {
              "Compliance": {
                  "ComplianceContributorCount": {
                      "CappedCount": 2,
                      "CapExceeded": false
                  },
                  "ComplianceType": "NON_COMPLIANT"
              },
              "ConfigRuleName": "instances-in-vpc"
          },
          {
              "Compliance": {
                  "ComplianceType": "COMPLIANT"
              },
              "ConfigRuleName": "restricted-common-ports"
          },
  ...
  ```

  For each rule that has a compliance type of `NON_COMPLIANT`, AWS Config returns the number of noncompliant resources for the `CappedCount` parameter\.
+ To see the compliance state of each resource that AWS Config evaluates for a specific rule, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/get-compliance-details-by-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/get-compliance-details-by-config-rule.html) command, as shown in the following example:

  ```
  $ aws configservice get-compliance-details-by-config-rule --config-rule-name ConfigRuleName{
      "EvaluationResults": [
          {
              "EvaluationResultIdentifier": {
                  "OrderingTimestamp": 1443610576.349,
                  "EvaluationResultQualifier": {
                      "ResourceType": "AWS::EC2::Instance",
                      "ResourceId": "i-nnnnnnnn",
                      "ConfigRuleName": "ConfigRuleName"
                  }
              },
              "ResultRecordedTime": 1443751424.969,
              "ConfigRuleInvokedTime": 1443751421.208,
              "ComplianceType": "COMPLIANT"
          },
          {
              "EvaluationResultIdentifier": {
                  "OrderingTimestamp": 1443610576.349,
                  "EvaluationResultQualifier": {
                      "ResourceType": "AWS::EC2::Instance",
                      "ResourceId": "i-nnnnnnnn",
                      "ConfigRuleName": "ConfigRuleName"
                  }
              },
              "ResultRecordedTime": 1443751425.083,
              "ConfigRuleInvokedTime": 1443751421.301,
              "ComplianceType": "NON_COMPLIANT"
          },
  ...
  ```
+ To see the compliance state for each AWS resource of a specific type, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-compliance-by-resource.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-compliance-by-resource.html) command, as shown in the following example:

  ```
  $ aws configservice describe-compliance-by-resource --resource-type AWS::EC2::Instance
  {
      "ComplianceByResources": [
          {
              "ResourceType": "AWS::EC2::Instance",
              "ResourceId": "i-nnnnnnnn",
              "Compliance": {
                  "ComplianceContributorCount": {
                      "CappedCount": 1,
                      "CapExceeded": false
                  },
                  "ComplianceType": "NON_COMPLIANT"
              }
          },
          {
              "ResourceType": "AWS::EC2::Instance",
              "ResourceId": "i-nnnnnnnn",
              "Compliance": {
                  "ComplianceType": "COMPLIANT"
              }
          },
  ...
  ```
+ To see the compliance details of an individual AWS resource, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/get-compliance-details-by-resource.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/get-compliance-details-by-resource.html) command\.

  ```
  $ aws configservice get-compliance-details-by-resource --resource-type AWS::EC2::Instance --resource-id i-nnnnnnnn
  {
      "EvaluationResults": [
          {
              "EvaluationResultIdentifier": {
                  "OrderingTimestamp": 1443610576.349,
                  "EvaluationResultQualifier": {
                      "ResourceType": "AWS::EC2::Instance",
                      "ResourceId": "i-nnnnnnnn",
                      "ConfigRuleName": "instances-in-vpc"
                  }
              },
              "ResultRecordedTime": 1443751425.083,
              "ConfigRuleInvokedTime": 1443751421.301,
              "ComplianceType": "NON_COMPLIANT"
          }
      ]
  }
  ```

**Example To view compliance \(AWS Config API\)**  
To view compliance, use any of the following API actions:  
+ To see the compliance state of each of your rules, use the [DescribeComplianceByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByConfigRule.html) action\.
+ To see the compliance state of each resource that AWS Config evaluates for a specific rule, use the [GetComplianceDetailsByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByConfigRule.html) action\.
+ To see the compliance state for each AWS resource of a specific type, use the [DescribeComplianceByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByResource.html) action\.
+ To see the compliance details of an individual AWS resource, use the [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html) action\. The details include which AWS Config rules evaluated the resource, when each rule last evaluated it, and whether the resource complies with each rule\.