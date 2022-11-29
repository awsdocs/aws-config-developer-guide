# Turning on AWS Config<a name="gs-cli-subscribe"></a>

**Note**  
Before setting up AWS Config with the AWS CLI, you need to create an Amazon S3 bucket, an Amazon SNS topic, and an IAM role with attached policies as prerequisites\. You can then use the AWS CLI to specify the bucket, topic, and role for AWS Config\. To set up your prerequisites for AWS Config, see [Prerequisites](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli-prereq.html)\.

To turn on AWS Config with the AWS CLI, use the [put\-configuration\-recorder](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html), [put\-delivery\-channel](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html), and [start\-configuration\-recorder](https://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) commands\.

The `put-configuration-recorder` command creates a new configuration recorder to record your selected resource configurations\. The `put-delivery-channel` command creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic\. You can have one configuration recorder and one delivery channel per region in your account\. Once a delivery channel is created, the `start-configuration-recorder` starts recording your selected resource configurations which you can see in your AWS account\.

You can specify the name of the recorder and the Amazon Resource Name \(ARN\) of the IAM role used to describe the AWS resources associated with the account\. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder\. You cannot change the assigned name\.

To set up AWS Config for Multi\-Account Multi\-Region Data Aggregation with the AWS CLI, see [Setting Up an Aggregator Using the AWS Command Line Interface](https://docs.aws.amazon.com/config/latest/developerguide/set-up-aggregator-cli.html)\. A separate configuration recorder will need to be created for each region in each AWS account that you would want to record configuration items\.

**Contents**
+ [put\-configuration\-recorder](#gs-cli-subscribe-put-configuration-recorder)
+ [put\-delivery\-channel](#gs-cli-subscribe-put-delivery-channel)
+ [start\-configuration\-recorder](#gs-cli-subscribe-start-configuration-recorder)

## put\-configuration\-recorder<a name="gs-cli-subscribe-put-configuration-recorder"></a>

Your [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command should look like the following example:

```
$ aws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=arn:aws:iam::123456789012:role/config-role --recording-group allSupported=true,includeGlobalResourceTypes=true
```

This command uses the following options for the `--recording-group` parameter:
+ `allSupported=true` – AWS Config records configuration changes for every supported type of *regional resource*\. When AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type\.
+ `includeGlobalResourceTypes=true` – AWS Config includes supported types of global resources with the resources that it records\. When AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type\.

  Before you can set this option to `true`, you must set the `allSupported` option to `true`\.

  If you do not want to include global resources, set this option to `false`, or omit it\.
**Note**  
**Pre\-existing AWS Config role**  
If you have used an AWS service that uses AWS Config, such as AWS Security Hub or AWS Control Tower, and an AWS Config role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the already created AWS Config role\. You must do this so that the other AWS service continues to run as expected\.   
For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon Simple Storage Service \(Amazon S3\) objects, make sure that the same permissions are granted within the IAM role you use when setting up AWS Config\. Otherwise, it may interfere with how AWS Control Tower operates\. For more information about IAM roles for AWS Config, see [AWS Identity and Access Management](https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html)\. 

## put\-delivery\-channel<a name="gs-cli-subscribe-put-delivery-channel"></a>

To setup the delivery channel, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) command:

```
$ aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json
```

The deliveryChannel\.json file specifies the delivery channel attributes:

```
{
    "name": "default",
    "s3BucketName": "config-bucket-123456789012",
    "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}
```

This example sets the following attributes:
+ `name` – The name of the delivery channel\. By default, AWS Config assigns the name `default` to a new delivery channel\.

  You cannot update the delivery channel name with the `put-delivery-channel` command\. For the steps to change the name, see [Renaming the Delivery Channel](manage-delivery-channel.md#update-dc-rename)\.
+ `s3BucketName` – The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files\.

  If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)\.
+ `snsTopicARN` – The Amazon Resource Name \(ARN\) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes\.

  If you choose a topic from another account, that topic must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md)\.
+ `configSnapshotDeliveryProperties` – Contains the `deliveryFrequency` attribute, which sets how often AWS Config delivers configuration snapshots\.

## start\-configuration\-recorder<a name="gs-cli-subscribe-start-configuration-recorder"></a>

To finish turning on AWS Config, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) command:

```
$ aws configservice start-configuration-recorder --configuration-recorder-name configRecorderName
```