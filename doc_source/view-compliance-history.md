# Viewing Compliance History Timeline for Resources<a name="view-compliance-history"></a>

AWS Config supports storing compliance state changes of resources as evaluated by AWS Config Rules\. The resource compliance history is presented in the form of a timeline\. The timeline captures changes as `ConfigurationItems` over a period of time for a specific resource\. For information on the contents of `ConfigurationItem`, see [ConfigurationItem](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in the AWS Config API Reference\.

You can opt in or out to record all resource types in AWS Config\. If you have opted to record all resource types, AWS Config automatically begins to recording the resource compliance history as evaluated by AWS Config Rules\. By default, AWS Config records the configuration changes for all supported resources\. You can also select only the specific resource compliance history resource type: `AWS::Config::ResourceCompliance`\. For more information, see [Selecting Which Resources AWS Config Records](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-console)\.

## Viewing Resource Timeline Using Resources<a name="resources-route-compliance-history"></a>

Access the resource timeline by selecting a specific resource from the Resource inventory page\.

1. Choose the **Resources** from the left navigation\.

1. On the Resource inventory page, you can filter by resource category, resource type, and compliance status\. Choose **Include deleted resources** if appropriate\.

   The table displays the resource identifier for the resource type and the resource compliance status for that resource\. The resource identifier might be a resource ID or a resource name\.

1. Choose a resource from the resource identifier column\.

1. Choose the **Resource Timeline** button\. You can filter by Configuration events, Compliance events, or CloudTrail Events\.
**Note**  
Alternatively, on the Resource inventory page, you can directly choose the resource name\. To access the resource timeline from the resource details page, choose the **Resource Timeline** button\.

## Viewing Resource Timeline Using Rules<a name="rules-route-compliance-history"></a>

Access the resource timeline by selecting a specific rule from the Rule page\.

1. Select the **Rules** from the left navigation\.

1. On the Rule page, choose a rule evaluating your relevant resources\. If no rules are displayed on the screen, add rules using the **Add rule** button\.

1. On the Rule details page, select the resources from the Resources evaluated table\.

1. Select the **Resource Timeline** button\. The resource timeline is displayed\.

## Querying Compliance History<a name="quering-resource-compliance-history"></a>

Query the resource compliance history using get\-resource\-config\-history using the resource type `AWS::Config::ResourceCompliance`\.

```
aws configservice get-resource-config-history --resource-type AWS::Config::ResourceCompliance --resource-id AWS::S3::Bucket/configrules-bucket
```

You should see output similar to the following:

```
{
	"configurationItems": [
		{
			"configurationItemCaptureTime": 1539799966.921,
			"relationships": [
				{
					"resourceType": "AWS::S3::Bucket",
					"resourceId": "configrules-bucket",
					"relationshipName": "Is associated with "
				}
			]
			"tags": {},
			"resourceType": "AWS::Config::ResourceCompliance",
			"resourceId": "AWS::S3::Bucket/configrules-bucket",
			"ConfigurationStateId": "1539799966921",
			"relatedEvents": [];
			"awsRegion": "us-west-2",
			"version": "1.3",
			"configurationItemMD5Hash": "",
			"supplementaryConfiguration": {},
			"configuaration": "{\"complianceType\":\"COMPLIANT\",\"targetResourceId\":\"configrules-bucket\",\"targetResourceType\":\"AWS::S3::Bucket\",\configRuleList"\":[{\"configRuleArn\":\"arn:aws:config:us-west-2:AccountID:config-rule/config-rule-w1gogw\",\"configRuleId\":\"config-rule-w1gogw\",\"configRuleName\":\"s3-bucket-logging-enabled\",\"complianceType\":\"COMPLIANT\"}]}",
			
			"configurationItemStatus": "ResourceDiscovered",
			"accountId": "AccountID"
		}
	]
}
```