# Deploying a Conformance Pack Using the AWS Command Line Interface<a name="conformance-pack-cli"></a>

You can deploy, view, update, view compliance status, and delete an AWS Config conformance pack using the AWS Command Line Interface \(AWS CLI\)\.

To install the AWS CLI on your local machine see, [AWS Config Conforms Amazon S3 bucket\.](https://s3.console.aws.amazon.com/s3/buckets/aws-config-conforms-docs)

If necessary, type `aws configure` to configure the AWS CLI to use an AWS Region where AWS Config conformance packs are available\.

**Topics**
+ [Deploy a Conformance Pack](#deploy-a-conformance-pack-cli)
+ [View a Conformance Pack](#view-a-conformance-pack)
+ [View Conformance Pack Status](#view-a-conformance-pack-status)
+ [View Conformance Pack Compliance Status](#view-a-conformance-pack-compliance-status)
+ [Get Compliance Details for a Specific Conformance Pack](#get-conformance-pack-compliance-details)
+ [Delete a Conformance Pack](#delete-a-conformance-pack-cli)

## Deploy a Conformance Pack<a name="deploy-a-conformance-pack-cli"></a>

1. Open a command prompt or a terminal window\.

1. Type the following command to deploy a conformance pack named **MyConformancePack1**\.

   ```
   aws configservice put-conformance-pack --conformance-pack-name="MyConformancePack1" --template-s3-uri="s3://AmazonS3bucketname/template name.yaml" --delivery-s3-bucket=AmazonS3bucketname
   ```

   OR

   You can also upload a YAML template from your local directory\.

   ```
   aws configservice put-conformance-pack --conformance-pack-name="MyConformancePack1" --template-body=template body --delivery-s3-bucket=AmazonS3bucketname
   ```

1. Press Enter to run the command\.

   You should see output similar to the following\.

   ```
   {
       "conformancePackArn": "arn:aws:config:us-west-2:AccountID:conformance-pack/MyConformancePack1/conformance-pack-ID"
   }
   ```

## View a Conformance Pack<a name="view-a-conformance-pack"></a>

1. Type the following command\.

   ```
   aws configservice describe-conformance-packs 
   ```

   OR

   ```
   aws configservice describe-conformance-packs --conformance-pack-name="MyConformancePack1"
   ```

1. You should see output similar to the following\.

   ```
   {
       "conformancePackName": "MyConformancePack1",
       "conformancePackId": "conformance-pack-ID",
       "conformancePackArn": "arn:aws:config:us-west-2:AccountID:conformance-pack/MyConformancePack1/conformance-pack-ID",
       "conformancePackInputParameters": [],
       "lastUpdateRequestedTime": "Thu Jul 18 16:07:05 PDT 2019"
   }
   ```

## View Conformance Pack Status<a name="view-a-conformance-pack-status"></a>

1. Type the following command\.

   ```
   aws configservice describe-conformance-pack-status --conformance-pack-name="MyConformancePack1"
   ```

1. You should see output similar to the following \.

   ```
   {
       "stackArn": "arn:aws:cloudformation:us-west-2:AccountID:stack/awsconfigconforms-MyConformancePack1-conformance-pack-ID/d4301fe0-a9b1-11e9-994d-025f28dd83ba",
       "conformancePackName": "MyConformancePack1",
       "conformancePackId": "conformance-pack-ID",
       "lastUpdateCompletedTime": "Thu Jul 18 16:15:17 PDT 2019",
       "conformancePackState": "CREATE_COMPLETE",
       "conformancePackArn": "arn:aws:config:us-west-2:AccountID:conformance-pack/MyConformancePack1/conformance-pack-ID",
       "lastUpdateRequestedTime": "Thu Jul 18 16:14:35 PDT 2019"
   }
   ```

## View Conformance Pack Compliance Status<a name="view-a-conformance-pack-compliance-status"></a>

1. Type the following command\.

   ```
   aws configservice describe-conformance-pack-compliance --conformance-pack-name="MyConformancePack1"
   ```

1. You should see output similar to the following\.

   ```
   {
       "conformancePackName": "MyConformancePack1",
       "conformancePackRuleComplianceList": [
           {
               "configRuleName": "awsconfigconforms-RuleName1-conformance-pack-ID",
               "complianceType": "NON_COMPLIANT"
           },
           {
               "configRuleName": "awsconfigconforms-RuleName2-conformance-pack-ID",
               "complianceType": "COMPLIANT"
           }
       ]
   }
   ```

## Get Compliance Details for a Specific Conformance Pack<a name="get-conformance-pack-compliance-details"></a>

1. Type the following command\.

   ```
   aws configservice get-conformance-pack-compliance-details --conformance-pack-name="MyConformancePack1"
   ```

1. You should see output similar to the following\.

   ```
   {
       "conformancePackRuleEvaluationResults": [
           {
               "evaluationResultIdentifier": {
                   "orderingTimestamp": "Tue Jul 16 23:07:35 PDT 2019",
                   "evaluationResultQualifier": {
                       "resourceId": "resourceID",
                       "configRuleName": "awsconfigconforms-RuleName1-conformance-pack-ID",
                       "resourceType": "AWS::::Account"
                   }
               },
               "configRuleInvokedTime": "Tue Jul 16 23:07:50 PDT 2019",
               "resultRecordedTime": "Tue Jul 16 23:07:51 PDT 2019",
               "complianceType": "NON_COMPLIANT"
           },
           {
               "evaluationResultIdentifier": {
                   "orderingTimestamp": "Thu Jun 27 15:16:36 PDT 2019",
                   "evaluationResultQualifier": {
                       "resourceId": "resourceID",
                       "configRuleName": "awsconfigconforms-RuleName2-conformance-pack-ID",
                       "resourceType": "AWS::EC2::SecurityGroup"
                   }
               },
              "configRuleInvokedTime": "Thu Jul 11 23:08:06 PDT 2019",
               "resultRecordedTime": "Thu Jul 11 23:08:06 PDT 2019",
               "complianceType": "COMPLIANT"
           }
       ],
       "conformancePackName": "MyConformancePack1"
   }
   }
   ```

## Delete a Conformance Pack<a name="delete-a-conformance-pack-cli"></a>
+ Type the following command\.

  ```
  aws configservice delete-conformance-pack --conformance-pack-name MyConformancePack1
  ```

  If successful, the command runs with no additional output\.