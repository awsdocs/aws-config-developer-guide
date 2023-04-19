# Conformance Packs<a name="conformance-packs"></a>

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organization in AWS Organizations\.

Conformance packs are created by authoring a YAML template that contains the list of AWS Config managed or custom rules and remediation actions\. You can deploy the template by using the AWS Config console or the AWS CLI\. To quickly get started and to evaluate your AWS environment, use one of the [sample conformance pack templates](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html)\. You can also create a conformance pack YAML file from scratch based on [Custom Conformance Pack](https://docs.aws.amazon.com/config/latest/developerguide/custom-conformance-pack.html)\.

**Topics**
+ [Prerequisites](cpack-prerequisites.md)
+ [Region Support](#conformance-packs-regions)
+ [AWS Config Process Checks Within a Conformance Pack](process-checks.md)
+ [Conformance Pack Sample Templates](conformancepack-sample-templates.md)
+ [Custom Conformance Pack](custom-conformance-pack.md)
+ [Viewing Compliance Data in the Conformance Packs Dashboard](conformance-pack-dashboard.md)
+ [Deploying a Conformance Pack Using the AWS Config Console](conformance-pack-console.md)
+ [Deploying a Conformance Pack Using the AWS Command Line Interface](conformance-pack-cli.md)
+ [Managing Conformance Packs \(API\)](conformance-pack-apis.md)
+ [Managing Conformance Packs Across all Accounts in Your Organization](conformance-pack-organization-apis.md)
+ [Viewing the Compliance History Timeline for Conformance Packs](compliance-history-conformance-pack.md)
+ [Troubleshooting](#w2aac14c35)

## Region Support<a name="conformance-packs-regions"></a>

Conformance packs are supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)

Deploying conformance packs across member accounts in an AWS Organization is supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)

## Troubleshooting<a name="w2aac14c35"></a>

If you get an error indicating that the conformance pack failed while creating, updating, or deleting it, you can check the status of your conformance pack\.

```
aws configservice describe-conformance-pack-status --conformance-pack-name MyConformancePack1
```

You should see output similar to the following\.

```
"ConformancePackStatusDetails": [
    {
        "ConformancePackName": "ConformancePackName",
        "ConformancePackId": "ConformancePackId",
        "ConformancePackArn": "ConformancePackArn",
        "ConformancePackState": "CREATE_FAILED",
        "StackArn": "CloudFormation stackArn",
        "ConformancePackStatusReason": "Failure Reason",
        "LastUpdateRequestedTime": 1573865201.619,
        "LastUpdateCompletedTime": 1573864244.653
    }
]
```

Check the **ConformancePackStatusReason** for information about the failure\. 

**When the stackArn is present in the response**

If the error message is not clear or if the failure is due to an internal error, go to the AWS CloudFormation console and do the following:

1. Search for the **stackArn** from the output\.

1. Choose the **Events** tab of the AWS CloudFormation stack and check for failed events\.

   The status reason indicates why the conformance pack failed\.

**When the stackArn is not present in the response**

If you receive a failure while you create a conformance pack but the stackArn is not present in the status response, the possible reason is that the stack creation failed and AWS CloudFormation rolled back and deleted the stack\. Go to the AWS CloudFormation console and search for stacks that are in a **Deleted** state\. The failed stack might be available there\. The AWS CloudFormation stack contains the conformance pack name\. If you find the failed stack, choose the **Events** tab of the AWS CloudFormation stack and check for failed events\.

If none of these steps worked and if the failure reason is an internal service error, then try operation again or contact AWS Config support\.
