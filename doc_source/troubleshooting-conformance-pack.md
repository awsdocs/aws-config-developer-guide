# Troubleshooting<a name="troubleshooting-conformance-pack"></a>

If you get an error indicating that the conformance pack failed while creating, updating, or deleting it, you can check the status of your conformance pack\.

```
aws configservice describe-conformance-pack-status --conformance-pack-name=ConformancePackName
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