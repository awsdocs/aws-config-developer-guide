# Looking Up Resources That Are Discovered by AWS Config<a name="looking-up-discovered-resources"></a>

You can use the AWS Config console, AWS CLI, and AWS Config API to look up the resources that AWS Config has taken an inventory of, or *discovered*, including deleted resources and resources that AWS Config is not currently recording\. AWS Config discovers supported resource types only\. For more information, see [Supported Resource Types](resource-config-reference.md)\.

## Looking Up Resources \(AWS Config Console\)<a name="looking-up-resources"></a>

You can use resource types or tag information to look up resources in the AWS Config console\.

**To look up resources**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. On the **Resource inventory** page, specify the search options for the resources that you want to look up:
   + Choose **Resources** and then choose one or more resource types in the list\. This list includes resource types that AWS Config supports\. To narrow results, type a resource ID or, if applicable, a resource name in the next box\. You can also choose **Include deleted resources**\. 
   + Choose **Tag** and type a tag key that is applied to your resources, such as **CostCenter**\. To narrow results, type a tag value in the next box\.

1. After you specify the search options, choose **Look up**\.

1. AWS Config lists the resources that match your search options\. You can see the following information about the resources:
   + **Resource identifier** – The resource identifier might be a resource ID or a resource name, if applicable\. Choose the resource identifier link to view the resource details page\. 
   + **Resource type** – The type of the resource is listed\.
   + **Compliance** – The status of the resource that AWS Config evaluated against your rule\.

     For more information, see [Viewing Configuration Details](view-manage-resource-console.md)\.

## Looking Up Resources \(AWS CLI\)<a name="looking-up-resources-with-the-aws-cli"></a>

You can use the AWS CLI to list resources that AWS Config has discovered\. 

**To look up resources \(AWS CLI\)**
+ Use the aws configservice [http://docs.aws.amazon.com/cli/latest/reference/configservice/list-discovered-resources.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/list-discovered-resources.html) command:  
**Example**  

  ```
  $ aws configservice list-discovered-resources --resource-type "AWS::EC2::Instance"
          {
              "resourceIdentifiers": [
                  {
                      "resourceType": "AWS::EC2::Instance",
                      "resourceId": "i-nnnnnnnn"
                  }
              ]
          }
  ```

To view the configuration details of a resource that is listed in the response, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/get-resource-config-history.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/get-resource-config-history.html) command, and specify the resource type and ID\. For an example of this command and the response from AWS Config, see [Viewing Configuration History](view-manage-resource-console.md#get-config-history-cli)\.

## Looking up Resources \(AWS Config API\)<a name="looking-up-resources-with-aws-config-api"></a>

You specify a resource type, and AWS Config returns a list of resource identifiers for resources of that type\. For more information, see [ResourceIdentifier](https://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html) in the *AWS Config API Reference*\.

**To look up resources \(AWS Config API\)**
+ Use the [ListDiscoveredResources](https://docs.aws.amazon.com/config/latest/APIReference/API_ListDiscoveredResources.html) action\.

To get the configuration details of a resource that is listed in the response, use the [GetResourceConfigHistory](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceConfigHistory.html) action, and specify the resource type and ID\.