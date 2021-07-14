# Viewing Compliance History Timeline for Conformance Packs<a name="compliance-history-conformance-pack"></a>

AWS Config supports storing compliance state changes to your conformance packs\. This allows you to view the history of compliance state changes and adjust remediation actions to meet compliance goals\. These compliance state changes are presented as a timeline\. The timeline captures changes as `ConfigurationItems` over a period of time\. You can also use this feature to find specific rules within a conformance pack that are non\-compliant\.

You can opt in or out to record all resource types in AWS Config\. If you have opted to record all resource types, AWS Config automatically begins recording the conformance pack compliance history as evaluated by AWS Config Rules\. By default, AWS Config records the configuration changes for all supported resources\. You can also select only the specific conformance pack compliance history resource type: `AWS::Config::ConformancePackCompliance`\. Recording for the `AWS::Config::ConformancePackCompliance` resource type is available at no additional charge\. For more information, see [Selecting Which Resources AWS Config Records](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-console)\.

A conformance pack is compliant if all of the rules in a conformance packs are compliant\. It is noncompliant if any of the rules are not compliant\. The compliance status of a conformance pack is INSUFFICIENT\_DATA only if all rules within a conformance pack cannot be evaluated due to insufficient data\. If some of the rules in a conformance pack are compliant but the compliance status of other rules in that same conformance pack is INSUFFICIENT\_DATA, the conformance pack shows compliant\. Compliance for a conformance pack is not evaluated all at once\. Some rules may take a longer time to evaluate than others\. Compliance is evaluated for groups of rules at a time, continuing in stages until all the rules in a conformance pack have been evaluated\.

**Topics**
+ [Viewing the Compliance Timeline](#viewing-compliance-history-conformance-pack)
+ [Querying Compliance History](#querying-compliance-history-conformance-pack)

## Viewing the Compliance Timeline<a name="viewing-compliance-history-conformance-pack"></a>

Access the compliance timeline by selecting a specific conformance pack from the **Conformance pack** main page\.

1. Navigate to the **Conformance Pack** page\.

1. On the **Conformance Pack** main page, choose a specific conformance pack and then choose **Conformance pack timeline** \.
**Note**  
Alternatively, you can use the compliance timeline from the conformance pack's details page\. Choose a conformance pack and choose **View details** in the **Actions** dropdown\. From this page, choose **Conformance pack timeline**\.

The timeline shows you the history of compliance state changes for a conformance pack\. You can do the following:

1. Adjust remediation actions to meet compliance goals\.

1. Expand a compliance change to view the line\-by\-line compliance status of each rule within a conformance pack\.

1. From the expanded view, choose a specific rule to view its details page\.

## Querying Compliance History<a name="querying-compliance-history-conformance-pack"></a>

Query the compliance history using get\-resource\-config\-history using the resource type `AWS::Config::ConformancePackCompliance`\.

```
aws configservice get-resource-config-history --resource-type AWS::Config::ConformancePackCompliance --resource-id conformance-pack-ID
```

You should see output similar to the following:

```
{
    "configurationItems": [
        {
            "version": "1.3",
            "accountId": "Account ID",
            "configurationItemCaptureTime": 1614641951.442,
            "configurationItemStatus": "OK",
            "configurationStateId": "1614641951442",
            "configurationItemMD5Hash": "",
            "arn": "arn:aws:config:us-east-1:Account ID:conformance-pack/MyConformancePack1/conformance-pack-ID",
            "resourceType": "AWS::Config::ConformancePackCompliance",
            "resourceId": "conformance-pack-ID",
            "resourceName": "MyConformancePack1",
            "awsRegion": "us-east-1",
            "tags": {},
            "relatedEvents": [],
            "relationships": [],
            "configuration": "{\"compliantRuleCount\":1,\"configRuleList\":[{\"configRuleName\":\"RuleName1-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-nnnnnn\",\"complianceType\":\"INSUFFICIENT_DATA\"},{\"configRuleName\":\"RuleName2-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-mmmmmm\",\"complianceType\":\"COMPLIANT\"},{\"configRuleName\":\"RuleName3-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-pppppp\",\"complianceType\":\"INSUFFICIENT_DATA\"}],\"totalRuleCount\":3,\"nonCompliantRuleCount\":0,\"complianceType\":\"COMPLIANT\"}",
            "supplementaryConfiguration": {}
        },
        {
            "version": "1.3",
            "accountId": "768311917693",
            "configurationItemCaptureTime": 1605551029.515,
            "configurationItemStatus": "ResourceDiscovered",
            "configurationStateId": "1605551029515",
            "configurationItemMD5Hash": "",
            "resourceType": "AWS::Config::ConformancePackCompliance",
            "resourceId": "conformance-pack-ID",
            "resourceName": "MyConformancePack1",
            "awsRegion": "us-east-1",
            "tags": {},
            "relatedEvents": [],
            "relationships": [],
            "configuration": "{\"compliantRuleCount\":1,\"configRuleList\":[{\"configRuleName\":\"RuleName1-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-nnnnnn\",\"complianceType\":\"INSUFFICIENT_DATA\"},{\"configRuleName\":\"RuleName2-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-mmmmmm\",\"complianceType\":\"COMPLIANT\"},{\"configRuleName\":\"RuleName3-conformance-pack-ID\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:Account ID:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-pppppp\",\"complianceType\":\"INSUFFICIENT_DATA\"}],\"totalRuleCount\":3,\"nonCompliantRuleCount\":0,\"complianceType\":\"COMPLIANT\"}",
            "supplementaryConfiguration": {}
        }
    ]
}
```

For more information, see [Supported Resource Types \(AWS Config\)](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#awsconfig) and [GetResourceConfigHistory](https://docs.aws.amazon.com/config/latest/APIReference/APIReference/API_GetResourceConfigHistory.html) in the API reference\.