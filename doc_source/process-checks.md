# AWS Config Process Checks Within a Conformance Pack<a name="process-checks"></a>

Process checks is a type of AWS Config rule that allows you to track your external and internal tasks that require verification as part of the conformance packs\. These checks can be added to an existing conformance pack or a new conformance pack\. You can track all compliance that includes AWS Configurations and manual checks in a single location\. 

With process checks, you can list the compliance of requirements and actions at a single location\. These process checks help increase the coverage of compliance regimes\-based conformance packs\. You can further expand the conformance pack by adding new process checks that track processes and actions needing manual verification and tracking\. This enables conformance pack to become the template that provides details about AWS Configurations and manual processes for a compliance regime\.

  You can track and manage the compliance of processes not associated with resource configuration changes within a conformance packs as process checks\. For example, you can add a process check to track the PCI\-DSS compliance requirement to store media backup at an offsite location\. You will manually evaluate the compliance of this according to PCI\-DSS guidelines, or according to your organization's guidance\. 

**Region availability**: Process checks with the conformance packs are available in all AWS Regions where AWS Config conformance packs are available\. For more information, see [Region Support](conformance-packs.md#conformance-packs-regions)\.

**Topics**
+ [Sample Conformance Pack Template for Creating Process Checks](#Sample-CPack-Template-for-Creating-Process-Check-Rule)
+ [Include Process Checks Within a Conformance Pack](#How-to-create-a-Process-Check-Rule)
+ [Change Compliance Status of a Process Check](#change-compliance-status)
+ [View and Edit the Process Check \(Console\)](#view-a-process-check-console)

## Sample Conformance Pack Template for Creating Process Checks<a name="Sample-CPack-Template-for-Creating-Process-Check-Rule"></a>

```
################################################################################
#
#  Conformance Pack template for process check
#
################################################################################
Resources:
  AWSConfigProcessCheck:
    Properties:
      ConfigRuleName: RuleName
      Description: Description of Rule
      Source:
        Owner: AWS
        SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
    Type: AWS::Config::ConfigRule
```

See two sample templates, the [ Operational Best Practices for CIS AWS Foundations Benchmark v1\.3 Level 1 ](operational-best-practices-for-cis_aws_benchmark_level_1.md) template and the [ Operational Best Practices for CIS AWS Foundations Benchmark v1\.3 Level 2 ](operational-best-practices-for-cis_aws_benchmark_level_2.md) template\.

## Include Process Checks Within a Conformance Pack<a name="How-to-create-a-Process-Check-Rule"></a>

1. Add a process check in the conformance pack template\. Refer to the previous sample template\.

   ```
   Resources:
     ConfigEnabledAllRegions:
       Properties:
         ConfigRuleName: Config-Enabled-All-Regions
         Description: Ensure AWS Config is enabled in all Regions.
         Source:
           Owner: AWS
           SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
       Type: AWS::Config::ConfigRule
   ```

1. Enter the name for the process check\.

1. Enter the description for the process check\.

1. Deploy the conformance pack from the AWS Management Console\. For more information, see [Deploying a Conformance Pack Using the AWS Config Console](conformance-pack-console.md)\.
**Note**  
You can also deploy the conformance packs using the Command Line Interface \(AWS CLI\)\. For more information, see [Deploying a Conformance Pack Using the AWS Command Line Interface](conformance-pack-cli.md)\.

## Change Compliance Status of a Process Check<a name="change-compliance-status"></a>

### Change Compliance Status of a Process Check \(Console\)<a name="change-compliance-status-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Navigate to the AWS Config Rules page\.

1. Choose the name of the process check that you specified in the template along with the identifier in the conformance pack\. 
**Note**  
All the process checks from the same conformance pack have the same suffix\.

1. On the Rule details page, you cannot edit the rule but you can edit the compliance of the rule\. In the Manual compliance section, choose **Edit compliance**\.

1. Choose the appropriate compliance from the dropdown list\.

1. \(Optional\) Enter a description for the compliance status\.

1. Choose **Save**\.

After changing the compliance status, return to your conformance pack to view the process check and its description\.

### Change Compliance Status of a Process Check \(CLI\)<a name="change-compliance-status-cli"></a>

You can update the compliance of process checks within a conformance pack using the AWS Command Line Interface \(AWS CLI\)\. 

To install the AWS CLI on your local machine, see [Installing the AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS CLI User Guide*\.

If necessary, type `AWS Configure` to configure the AWS CLI to use an AWS Region where AWS Config conformance packs are available\.

1. Open a command prompt or a terminal window\.

1. Type the following command to update the compliance of a process check where `ComplianceResourceId` is your `Account ID`, and include the name of your rule\.

   ```
   aws configservice put-external-evaluation --config-rule-name process-check-rule-name  --external-evaluation ComplianceResourceType=AWS::::Account,ComplianceResourceId=Account ID,ComplianceType=NON_COMPLIANT,OrderingTimestamp=2020-12-17T00:10:00.000Z
   ```

1. Press Enter to run the command\.

### Change Compliance Status of a Process Check \(API\)<a name="change-compliance-status-api"></a>

After the deployment is complete, to update the evaluations and compliance of the process checks, use the `PutExternalEvaluation` API\. For more information, see [PutExternalEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_PutExternalEvaluation.html)\.

## View and Edit the Process Check \(Console\)<a name="view-a-process-check-console"></a>

You can view process checks only after a compliance state has been added to process checks\. Choose the specific conformance pack to view all the process checks within that conformance pack\. Here you can see a list of process checks that are in compliant and non\-compliant status\.

Because this is a service linked rule, you cannot edit the process check through the Rule details page\.

**Note**  
However, you can update the compliance of the process check by choosing **Edit Compliance** and selecting the appropriate value from Compliant, Non\-Compliant or Not\-Applicable\.

You can edit or delete a process check from the conformance pack where you added the process checks\.