# Viewing Configuration Details<a name="view-manage-resource-console"></a>

You can view the configuration, relationships, and number of changes made to a resource in the AWS Config console\. You can view the configuration history for a resource using AWS CLI\.

## Viewing Configuration Details \(Console\)<a name="view-config-details-console"></a>

When you look up resources on the **Resource inventory** page, click the resource name or ID in the resource identifier column to view the resource's details page\. The details page provides information about the configuration, relationships, and number of changes made to that resource\.

The blocks at the top of the page are collectively called the *timeline*\. The timeline shows the date and the time that the recording was made\.

![\[View the configuration details, relationships, and changes to resource types in the AWS Config console.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/resource-details-timeline.png)

**Details page features**

1. Click to scroll the timeline to an earlier point in the resource's configuration history\.

1. Click a timeline block to select that time period\. The descriptions in the **Configuration Details**, **Relationships**, and **Changes** sections comprise the configuration item of the selected resource at the selected time period\.

1. Click to return the timeline to the current time\. 

1. Click to view a configuration item by specifying a date \(and, if needed, time\) and then choose **Apply**\.

1. Click to navigate to the **Changes** section\. The number that follows **Changes** is the number of configuration changes that occurred for the resource between the selected time period and the previous block\.

1. Click to navigate to the **CloudTrail events** section\. The number that follows **Events** is the number of API events that occurred for the resource between the selected time period and the previous block\. You can see the API events that AWS CloudTrail logged for the last 90 days\. CloudTrail events that occurred prior to the last 90 days can't be viewed in the timeline\.

   For more information, see [Viewing Events with CloudTrail API Activity History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*\.

**Note**  
CloudTrail events may not be available for the following reasons:  
Verify that you have sufficient read permissions for CloudTrail\. For more information, see [Read\-only access](recommended-iam-permissions-using-aws-config-console-cli.md#read-only-config-permission)\.
There is a service issue and CloudTrail events can't be displayed at this time\. Try refreshing the page\.
You don't have a CloudTrail trail in this region or your trail is not enabled for logging\. For more information, see [Creating a Trail for the First Time](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*\. 

### Timeline Navigation Tips for the Selected Resource<a name="timeline-navigation"></a>

The following are tips for using the timeline to view information about the selected resource\.
+ Use the arrows at either end of the timeline to view the timeline blocks for configuration items that were recorded in other time periods\.
+ Choose **Configuration Details** to view the description of the selected resource\.
+ Choose **Relationships** to see a list of supported resources in the account that are related to the selected resource\. If the **Relationships** section doesn't expand, the selected resource was not related to another resource that was in your account during the selected time period\. 

  For more information, see [Resource Relationship](config-concepts.md#resource-relationship)\. 
+ If changes are indicated for the selected time period, choose **Changes** to view the configuration changes made to the resource\. The **Changes** section also lists the relationship changes that occurred as a result of configuration changes\.
+ Choose **CloudTrail** **events** to view information about API calls that involve the resource, such as the event time, the user name, and the event name\. For example, if AWS Config is recording IAM resource types, and an IAM role is updated, you can view the event to see the `UpdateRole` in the **Event name** column\.
+ In the **View event** column, you can also choose the **CloudTrail** link to view more information about the event in the CloudTrail console\. You must create a trail and enable logging for CloudTrail to view the events in the AWS Config timeline\. 
+ Choose **View Details** to view the configuration information in text or JSON format\. Click the arrows in the details window to see additional details\.

  For more information about the entries in the details window, see [Components of a Configuration Item](config-item-table.md)\.
+ Choose **Manage resources** to go to the console for the selected resource\. If you make a change to the resource, go back to the AWS Config console and choose **Now** to see the changes\. It can take up to 10 minutes to refresh the details page for the resource\.

  The console also provides details pages for supported resources that you do not include in the list of resources that AWS Config records\. The information on these details pages is limited and ongoing configuration changes are not shown\.

## Viewing Configuration Details \(AWS CLI\)<a name="view-config-details-cli"></a>

The configuration items that AWS Config records are delivered to the specified delivery channel on demand as a configuration snapshot and as a configuration stream\. You can use the AWS CLI to view history of configuration items for each resource\.

### Viewing Configuration History<a name="get-config-history-cli"></a>

Type the [http://docs.aws.amazon.com/cli/latest/reference/configservice/get-resource-config-history.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/get-resource-config-history.html) command and specify the resource type and the resource ID, for example:

```
$ aws configservice get-resource-config-history --resource-type AWS::EC2::SecurityGroup --resource-id sg-6fbb3807
{
    "configurationItems": [
        {
            "configurationItemCaptureTime": 1414708529.9219999,
            "relationships": [
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-7a3b232a",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-8b6eb2ab",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-c478efe5",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-e4cbe38d",
                    "relationshipName": "Is associated with Instance"
                }
            ],
            "availabilityZone": "Not Applicable",
            "tags": {},
            "resourceType": "AWS::EC2::SecurityGroup",
            "resourceId": "sg-6fbb3807",
            "configurationStateId": "1",
            "relatedEvents": [],
            "arn": "arn:aws:ec2:us-east-2:012345678912:security-group/default",
            "version": "1.0",
            "configurationItemMD5Hash": "860aa81fc3869e186b2ee00bc638a01a",
            "configuration": "{\"ownerId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\",\"description\":\"default group\",\"ipPermissions\":[{\"ipProtocol\":\"tcp\",\"fromPort\":80,\"toPort\":80,\"userIdGroupPairs\":[{\"userId\":\"amazon-elb\",\"groupName\":\"amazon-elb-sg\",\"groupId\":\"sg-843f59ed\"}],\"ipRanges\":[\"0.0.0.0/0\"]},{\"ipProtocol\":\"tcp\",\"fromPort\":0,\"toPort\":65535,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"udp\",\"fromPort\":0,\"toPort\":65535,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"icmp\",\"fromPort\":-1,\"toPort\":-1,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"tcp\",\"fromPort\":1433,\"toPort\":1433,\"userIdGroupPairs\":[],\"ipRanges\":[\"0.0.0.0/0\"]},{\"ipProtocol\":\"tcp\",\"fromPort\":3389,\"toPort\":3389,\"userIdGroupPairs\":[],\"ipRanges\":[\"207.171.160.0/19\"]}],\"ipPermissionsEgress\":[],\"vpcId\":null,\"tags\":[]}",
            "configurationItemStatus": "ResourceDiscovered",
            "accountId": "605053316265"
        }
    ],
    "nextToken": 
     ..........
```

For detailed explanation of the response fields, see [Components of a Configuration Item](config-item-table.md) and [Supported Resource Types](resource-config-reference.md)\.

### Example Amazon EBS Configuration History from AWS Config<a name="example-s3-config-history"></a>

AWS Config generates a set of files that each represent a resource type and lists all configuration changes for the resources of that type that AWS Config is recording\. AWS Config exports this resource\-centric configuration history as an object in the Amazon S3 bucket that you specified when you enabled AWS Config\. The configuration history file for each resource type contains the changes that were detected for the resources of that type since the last history file was delivered\. The history files are typically delivered every six hours\.

The following is an example of the contents of the Amazon S3 object that describes the configuration history of all the Amazon Elastic Block Store volumes in the current region for your AWS account\. The volumes in this account include `vol-ce676ccc` and `vol-cia007c`\. Volume `vol-ce676ccc` had two configuration changes since the previous history file was delivered while volume `vol-cia007c` had one change\.

```
{
    "fileVersion": "1.0",
    "requestId": "asudf8ow-4e34-4f32-afeb-0ace5bf3trye",
    "configurationItems": [
        {
            "snapshotVersion": "1.0",
            "resourceId": "vol-ce676ccc",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-ce676ccc",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T23:47:08.918Z",
            "configurationStateID": "3e660fdf-4e34-4f32-afeb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adb69edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04ad92281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T21:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344c463d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-ce676ccc",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T21:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-ce676ccc",
                        "instanceId": "i-344c463d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume1"
                    }
                ],
                "volumeType": "standard"
            }
        },
        {
            "configurationItemVersion": "1.0",
            "resourceId": "vol-ce676ccc",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-ce676ccc",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T21:47:08.918Z",
            "configurationItemState": "3e660fdf-4e34-4f32-sseb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-ad229edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04w292281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T21:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344c463d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-ce676ccc",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T21:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-ce676ccc",
                        "instanceId": "i-344c463d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume1"
                    }
                ],
                "volumeType": "standard"
            }
        },
        {
            "configurationItemVersion": "1.0",
            "resourceId": "vol-cia007c",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-cia007c",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T20:47:08.918Z",
            "configurationItemState": "3e660fdf-4e34-4f88-sseb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adjhk8edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a67u292281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T20:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344e563d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-cia007c",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T20:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-cia007c",
                        "instanceId": "i-344e563d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume2"
                    }
                ],
                "volumeType": "standard"
            }
        }
    ]
}
```