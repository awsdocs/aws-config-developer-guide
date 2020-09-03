# Viewing Compliance History for Resources as Evaluated by AWS Config Rules<a name="view-compliance-history"></a>

AWS Config supports storing compliance state changes of resources as evaluated by AWS Config Rules\. The resource compliance history is presented in the form of a timeline\. The timeline captures changes as `ConfigurationItems` over a period of time for a specific resource\. The Compliance timeline is available in the AWS Config console adjacent to the Configuration timeline\. 

You can opt in or opt out to record all resource types in AWS Config\. If you have opted to record all resource types, AWS Config will automatically begin to record the resource compliance history as evaluated by AWS Config Rules\. You can select all the resources or specific types of resources for which you want AWS Config to record configuration changes\. By default, AWS Config records the configuration changes for all supported resources\. 

**Topics**
+ [Recording Resource Types in the AWS Console](#recording-resource-types)
+ [Viewing Compliance Timeline Using Resources](#resources-route-compliance-history)
+ [Viewing Compliance Timeline Using Rules](#rules-route-compliance-history)
+ [Querying Resource Compliance History](#quering-resource-compliance-history)

## Recording Resource Types in the AWS Console<a name="recording-resource-types"></a>

On the **Settings** page, for **Resource types to record**, specify the AWS resource types you want AWS Config to record:
+ **All resources** – AWS Config records all supported resources with the following options:
  + **Record all resources supported in this region** – AWS Config records configuration changes for every supported type of regional resource\. When AWS Config adds support for a new resource type, AWS Config automatically starts recording resources of that type\.
  + **Include global resources** – AWS Config includes supported types of global resources with the resources that it records \(for example, IAM resources\)\. When AWS Config adds support for a new global resource type, AWS Config automatically starts recording resources of that type\.
+ **Specific types** – AWS Config records configuration changes for only the AWS resource types that you specify\. Choose resource type `Config:ResourceCompliance` to record compliance history\.

## Viewing Compliance Timeline Using Resources<a name="resources-route-compliance-history"></a>

Access the compliance timeline by selecting a specific resource from the Resource inventory page\.

1. Select the **Resources** from the left navigation\.

1. On the Resource inventory page, select all the existing resources from the drop\-down and if appropriate, select include deleted resources\.

1. Click **Lookup**\.

   The table displays the resource identifier for the resource type and the resource compliance status for that resource\. The resource identifier might be a resource ID or a resource name, if applicable\. 

1. Select the resource from the resource identifier column\.

1. Select the **Compliance timeline** from the Resource actions drop\-down\.

   The compliance timeline is displayed\.  
![\[View the compliance history.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/compliance-history-with-rules.png)
**Note**  
Alternatively, on the Resource inventory page, you can directly click the resource name\. The Resource details page is displayed\. To access the compliance timeline from the resource details page, click the **Compliance timeline** button\.  

![\[Resource details page\]](http://docs.aws.amazon.com/config/latest/developerguide/images/resource-details-page.png)

## Viewing Compliance Timeline Using Rules<a name="rules-route-compliance-history"></a>

Access the compliance timeline by selecting a specific rule from the Rule page\.

1. Select the **Rules** from the left navigation\.

1. On the Rule page, click the name of the rule evaluating your relevant resources\. If no rules are displayed on the screen, add rules using the **Add rule** button\.

1. On the Rule details page, select the resources from the Resources evaluated table\.

1. Select **Compliance timeline** from the Resource actions drop\-down\. The compliance timeline is displayed\.

## Querying Resource Compliance History<a name="quering-resource-compliance-history"></a>

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