# Deploying a Conformance Pack Using the AWS Command Line Interface<a name="conformance-pack-cli"></a>

You can deploy, view, update, view compliance status, and delete an AWS Config conformance pack using the AWS Command Line Interface \(AWS CLI\)\.

The AWS CLI is a unified tool to manage your AWS services\. With just one tool to download and configure, you can control multiple AWS services from the command line and use scripts to automate them\. For more information about the AWS CLI and for instructions on installing the AWS CLI tools, see the following in the *AWS Command Line Interface User Guide*\.
+ [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
+ [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) 

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

1. Type one of the following commands to deploy a conformance pack named **MyConformancePack**\. The template source is either an Amazon S3 URI, a template that you upload, or an AWS Systems Manager document \(SSM document\)\.

   **Amazon S3 URI**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-s3-uri "s3://AmazonS3bucketname/template name.yaml"
   --delivery-s3-bucket AmazonS3bucketname
   ```

   **YAML template from your local directory**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-body template body
   --delivery-s3-bucket AmazonS3bucketname
   ```

   **AWS Systems Manager Document \(Systems Manager Document\)**

   ```
   aws config put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-ssm-document-details MyConformancePackDocument
   --delivery-s3-bucket AmazonS3bucketname
   ```

1. Press Enter to run the command\.

   You should see output similar to the following\.

   ```
   {
       "conformancePackArn": "arn:aws:config:us-west-2:AccountID:conformance-pack/MyConformancePack1/conformance-pack-ID"
   }
   ```

**Note**  
For more information on creating a YAML template for a conformance pack, see [Custom Conformance Pack](https://docs.aws.amazon.com/config/latest/developerguide/custom-conformance-pack.html)\.

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
**Important**  
You cannot revert this action\. When you delete a conformance pack, you delete all of the AWS Config rules and remediation actions in that conformance pack\.