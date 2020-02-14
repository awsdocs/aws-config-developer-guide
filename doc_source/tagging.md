# Tagging Your AWS Config Resources<a name="tagging"></a>

A tag is a label that you assign to an AWS resource\. Each tag consists of a *key* and an optional *value*, both of which you define\. Tags make it easier to manage, search for, and filter resources\.

Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment\. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags you've assigned to it\. You can assign one or more tags to your AWS resources\. Each tag has an associated value\.

We recommend that you devise a set of tag keys that meets your needs for each resource type\. Using a consistent set of tag keys makes it easier for you to manage your AWS resources\. You can search and filter the resources based on the tags you add\.

Tags are interpreted strictly as a string of characters and are not automatically assigned to your resources\. You can edit tag keys and values, and you can remove tags from a resource at any time\. You can set the value of a tag to an empty string, but you can't set the value of a tag to null\. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value\. If you delete a resource, any tags for the resource are also deleted\. 

You can work with tags using the AWS Command Line Interface \(AWS CLI\) and the AWS Config API reference\. 

## Restrictions Related to Tagging<a name="config-limits-tagging"></a>

The following basic restrictions apply to tags\.


| Restriction | Description | 
| --- | --- | 
|  Maximum number of tags per resource  |  50  | 
|  Maximum key length  |  128 Unicode characters in UTF\-8  | 
|  Maximum value length  |  256 Unicode characters in UTF\-8  | 
|  Prefix restriction  |  Do not use the `aws:` prefix in your tag names or values because it is reserved for AWS use\. You can't edit or delete tag names or values with this prefix\. Tags with this prefix do not count against your tags per resource limit\.  | 
|  Character restrictions  |  Tags may only contain Unicode letters, digits, whitespace, or these symbols: `_ . : / = + - @`  | 

## Managing Tags with AWS Config API Actions<a name="config-limits-api"></a>

Tag based access controls are available for three resources `ConfigurationAggregator`, `AggregationAuthorization`, and `ConfigRule`\. Use the following to add, update, list, and delete the tags for your resources\.
+ [ListTagsForResource](https://docs.aws.amazon.com/config/latest/APIReference/API_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html)