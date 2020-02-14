# Components of a Configuration Item<a name="config-item-table"></a>

A configuration item consists of the following components\.


****  

| Component | Description | Contains | 
| --- | --- | --- | 
| Metadata | Information about this configuration item | [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) | 
| Attributes1 | Resource attributes | [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) | 
| Relationships | How the resource is related to other resources associated with the account | Description of the relationship, such as Amazon EBS volume vol\-1234567 is attached to an Amazon EC2 instance i\-a1b2c3d4 | 
| Current configuration | Information returned through a call to the Describe or List API of the resource | For example, DescribeVolumes API returns the following information about the volume: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) | 

**Notes**

1. A configuration item relationship does not include network flow or data flow dependencies\. Configuration items cannot be customized to represent your application architecture\. 

1. AWS Config does not record key–value tags for CloudTrail trail, CloudFront distribution, and CloudFront streaming distribution\.

1. As of Version 1\.3, the relatedEvents field is empty\. You can access the [LookupEvents API](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) in the *AWS CloudTrail API Reference* to retrieve the events for the resource\.

1. As of Version 1\.3, the configurationItemMD5Hash field is empty\. You can use the configurationStateId field to ensure you have the latest configuration item\.